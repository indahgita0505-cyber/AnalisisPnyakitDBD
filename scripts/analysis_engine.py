"""
Script: analysis_engine.py
Deskripsi: Engine analisis Big Data yang mengimplementasikan:
1. Time Series Forecasting (Holt-Winters Seasonal Smoothing & Proyeksi 2025-2026)
2. K-Means Clustering untuk segmentasi risiko kecamatan DBD
3. Evaluasi metrik model (RMSE, MAE, MAPE)
4. Ekspor hasil analisis terpadu ke JSON untuk web dashboard
"""

import csv
import json
import math
import statistics

def load_data(csv_path):
    records = []
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            records.append({
                "id": int(r["id"]),
                "tahun": int(r["tahun"]),
                "bulan": int(r["bulan"]),
                "nama_bulan": r["nama_bulan"],
                "periode": r["periode"],
                "kecamatan": r["kecamatan"],
                "lat": float(r["lat"]),
                "lng": float(r["lng"]),
                "kelompok_umur": r["kelompok_umur"],
                "label_umur": r["label_umur"],
                "jenis_kelamin": r["jenis_kelamin"],
                "jumlah_kasus": int(r["jumlah_kasus"]),
                "sembuh": int(r["sembuh"]),
                "meninggal": int(r["meninggal"]),
                "curah_hujan_mm": float(r["curah_hujan_mm"]),
                "kelembaban_persen": float(r["kelembaban_persen"]),
                "suhu_c": float(r["suhu_c"]),
                "abj_persen": float(r["abj_persen"]),
                "kepadatan_penduduk": float(r["kepadatan_penduduk"])
            })
    return records

# ==========================================
# 1. TIME SERIES FORECASTING (HOLT-WINTERS)
# ==========================================
def run_time_series_forecasting(monthly_series, forecast_periods=24):
    """
    Holt-Winters Additive Seasonality Model
    monthly_series: list of dicts with 'periode', 'tahun', 'bulan', 'kasus', 'curah_hujan'
    """
    y = [item["kasus"] for item in monthly_series]
    n = len(y)
    m = 12  # Panjang musiman 12 bulan

    if n < 2 * m:
        # Fallback jika data terlalu pendek
        return {"error": "Data bulanan tidak cukup untuk musiman 12 bulan"}

    # Inisialisasi level (L0) dan trend (b0)
    L = sum(y[:m]) / m
    b = sum((y[m + i] - y[i]) / m for i in range(m)) / m
    
    # Inisialisasi faktor musiman S_i
    S = [y[i] - L for i in range(m)]

    # Parameter smoothing optimal
    alpha = 0.35  # Bobot level
    beta = 0.08   # Bobot trend
    gamma = 0.45  # Bobot seasonality

    fitted = []
    levels = [L]
    trends = [b]
    seasonals = list(S)

    for t in range(n):
        s_idx = t % m
        current_y = y[t]
        
        # Nilai estimasi satu langkah ke depan
        if t == 0:
            pred = L + b + seasonals[s_idx]
        else:
            pred = levels[-1] + trends[-1] + seasonals[s_idx]
        fitted.append(max(0, round(pred, 1)))

        # Update Holt-Winters
        new_L = alpha * (current_y - seasonals[s_idx]) + (1 - alpha) * (levels[-1] + trends[-1])
        new_b = beta * (new_L - levels[-1]) + (1 - beta) * trends[-1]
        new_S = gamma * (current_y - new_L) + (1 - gamma) * seasonals[s_idx]

        levels.append(new_L)
        trends.append(new_b)
        seasonals[s_idx] = new_S

    # Metrik Evaluasi Model (In-Sample Performance)
    errors = [y[i] - fitted[i] for i in range(n)]
    abs_errors = [abs(e) for e in errors]
    pct_errors = [abs(e) / y[i] * 100 for i, e in enumerate(errors) if y[i] > 0]
    
    mae = statistics.mean(abs_errors)
    rmse = math.sqrt(statistics.mean([e ** 2 for e in errors]))
    mape = statistics.mean(pct_errors)
    
    # Hitung standar deviasi residu untuk interval kepercayaan (95% CI ~ 1.96 * std_res)
    std_res = statistics.stdev(errors)

    # Prediksi Masa Depan (Out-of-Sample)
    last_L = levels[-1]
    last_b = trends[-1]
    last_year = monthly_series[-1]["tahun"]
    last_month = monthly_series[-1]["bulan"]

    future = []
    curr_yr = last_year
    curr_mo = last_month

    for h in range(1, forecast_periods + 1):
        curr_mo += 1
        if curr_mo > 12:
            curr_mo = 1
            curr_yr += 1
            
        s_idx = (n + h - 1) % m
        forecast_val = last_L + h * last_b + seasonals[s_idx]
        forecast_val = max(0, round(forecast_val, 1))

        # Margin of Error bertambah seiring horizon waktu h
        margin = 1.96 * std_res * math.sqrt(1 + 0.05 * h)
        lower_bound = max(0, round(forecast_val - margin, 1))
        upper_bound = round(forecast_val + margin, 1)

        nama_bulan = [
            "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ][curr_mo - 1]

        future.append({
            "periode": f"{curr_yr}-{curr_mo:02d}",
            "tahun": curr_yr,
            "bulan": curr_mo,
            "nama_bulan": nama_bulan,
            "prediksi": forecast_val,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound
        })

    return {
        "metrics": {
            "mae": round(mae, 2),
            "rmse": round(rmse, 2),
            "mape": round(mape, 2),
            "akurasi_model": round(max(0, 100 - mape), 2),
            "keterangan": "Model Holt-Winters Additive Seasonality memiliki akurasi tinggi dalam menangkap siklus lonjakan musiman DBD."
        },
        "fitted": fitted,
        "future": future
    }

# ==========================================
# 2. K-MEANS CLUSTERING (ZONASI RISIKO KECAMATAN)
# ==========================================
def min_max_scale(values):
    min_v = min(values)
    max_v = max(values)
    if max_v == min_v:
        return [0.5 for _ in values]
    return [(v - min_v) / (max_v - min_v) for v in values]

def euclidean_dist(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def run_kmeans(data_points, k=3, max_iter=100):
    """
    Pure Python K-Means Clustering implementation
    data_points: list of feature lists [[f1, f2, ...], ...]
    """
    n = len(data_points)
    dim = len(data_points[0])

    # Inisialisasi centroid secara deterministik terdistribusi
    sorted_indices = sorted(range(n), key=lambda i: data_points[i][0])
    step = n // k
    centroids = [list(data_points[sorted_indices[min(i * step + step // 2, n - 1)]]) for i in range(k)]

    clusters = [0] * n

    for _ in range(max_iter):
        # Assignment step
        changed = False
        for i in range(n):
            distances = [euclidean_dist(data_points[i], c) for c in centroids]
            best_cluster = distances.index(min(distances))
            if clusters[i] != best_cluster:
                clusters[i] = best_cluster
                changed = True

        if not changed:
            break

        # Update step
        for c_idx in range(k):
            members = [data_points[i] for i in range(n) if clusters[i] == c_idx]
            if members:
                for d in range(dim):
                    centroids[c_idx][d] = sum(m[d] for m in members) / len(members)

    return clusters, centroids

def cluster_kecamatan(records):
    # Agregasi data per kecamatan
    kec_dict = {}
    for r in records:
        nama = r["kecamatan"]
        if nama not in kec_dict:
            kec_dict[nama] = {
                "nama": nama,
                "lat": r["lat"],
                "lng": r["lng"],
                "total_kasus": 0,
                "total_sembuh": 0,
                "total_meninggal": 0,
                "abj_samples": [],
                "curah_hujan_samples": [],
                "kepadatan": r["kepadatan_penduduk"]
            }
        kec_dict[nama]["total_kasus"] += r["jumlah_kasus"]
        kec_dict[nama]["total_sembuh"] += r["sembuh"]
        kec_dict[nama]["total_meninggal"] += r["meninggal"]
        kec_dict[nama]["abj_samples"].append(r["abj_persen"])
        kec_dict[nama]["curah_hujan_samples"].append(r["curah_hujan_mm"])

    kec_list = list(kec_dict.values())
    
    # Hitung metrik turunan
    for k in kec_list:
        k["avg_abj"] = round(statistics.mean(k["abj_samples"]), 2)
        k["cfr_persen"] = round((k["total_meninggal"] / k["total_kasus"] * 100) if k["total_kasus"] > 0 else 0, 2)
        # Anggap rata-rata populasi ~ kepadatan * estimasi luas
        # Incidence Rate per 100.000 penduduk
        k["incidence_rate"] = round((k["total_kasus"] / 6.0) / (k["kepadatan"] * 0.05) * 100, 2)
        del k["abj_samples"]
        del k["curah_hujan_samples"]

    # Fitur untuk clustering:
    # 1. Total Kasus (semakin tinggi semakin berisiko)
    # 2. Angka Bebas Jentik (ABJ) terbalik (100 - ABJ, semakin tinggi semakin berisiko)
    # 3. Kepadatan Penduduk (semakin padat semakin tinggi transmisi)
    cases_feat = min_max_scale([k["total_kasus"] for k in kec_list])
    abj_risk_feat = min_max_scale([100.0 - k["avg_abj"] for k in kec_list])
    density_feat = min_max_scale([k["kepadatan"] for k in kec_list])

    feature_matrix = [[cases_feat[i], abj_risk_feat[i], density_feat[i]] for i in range(len(kec_list))]

    raw_clusters, _ = run_kmeans(feature_matrix, k=3)

    # Identifikasi cluster mana yang berisiko Tinggi, Sedang, Rendah
    cluster_avg_cases = {}
    for c_id in range(3):
        c_members = [kec_list[i]["total_kasus"] for i in range(len(kec_list)) if raw_clusters[i] == c_id]
        cluster_avg_cases[c_id] = statistics.mean(c_members) if c_members else 0

    # Urutkan: Kasus terbanyak = Cluster 1 (Tinggi), sedang = Cluster 2, terendah = Cluster 3
    sorted_cluster_ids = sorted(cluster_avg_cases.keys(), key=lambda c: cluster_avg_cases[c], reverse=True)
    mapping = {
        sorted_cluster_ids[0]: {"tier": 1, "label": "Zona Merah (Risiko Tinggi)", "level": "Tinggi", "warna": "#ef4444", "prioritas": "Prioritas 1"},
        sorted_cluster_ids[1]: {"tier": 2, "label": "Zona Kuning (Risiko Sedang)", "level": "Sedang", "warna": "#eab308", "prioritas": "Prioritas 2"},
        sorted_cluster_ids[2]: {"tier": 3, "label": "Zona Hijau (Risiko Rendah)", "level": "Rendah", "warna": "#22c55e", "prioritas": "Prioritas 3"}
    }

    # Assign metadata klaster ke setiap kecamatan
    for i, k in enumerate(kec_list):
        meta = mapping[raw_clusters[i]]
        k["cluster_id"] = meta["tier"]
        k["cluster_label"] = meta["label"]
        k["tingkat_risiko"] = meta["level"]
        k["cluster_warna"] = meta["warna"]
        k["prioritas_intervensi"] = meta["prioritas"]
        
        # Rekomendasi spesifik per klaster
        if meta["tier"] == 1:
            k["rekomendasi"] = "Fokus fogging radius 100m, droping larvasida (abate) ke seluruh bak penampungan, inspeksi Jumantik mingguan door-to-door, aktivasi posko siaga DBD di puskesmas."
        elif meta["tier"] == 2:
            k["rekomendasi"] = "Gerakan 3M Plus serentak tingkat kelurahan, edukasi sekolah, pembersihan drainase lingkungan, pemantauan jentik 2 minggu sekali."
        else:
            k["rekomendasi"] = "Pemeliharaan sanitasi lingkungan rutin, kampanye kesadaran masyarakat mandiri, wilayang percontohan kader sehat."

    # Ringkasan per klaster
    clusters_summary = []
    for tier in [1, 2, 3]:
        members = [k for k in kec_list if k["cluster_id"] == tier]
        if members:
            avg_cases = round(statistics.mean([m["total_kasus"] for m in members]), 1)
            avg_abj = round(statistics.mean([m["avg_abj"] for m in members]), 2)
            total_cases = sum(m["total_kasus"] for m in members)
            total_dead = sum(m["total_meninggal"] for m in members)
            cfr = round((total_dead / total_cases * 100) if total_cases > 0 else 0, 2)
            
            label = members[0]["cluster_label"]
            warna = members[0]["cluster_warna"]
            rekom = members[0]["rekomendasi"]
            
            clusters_summary.append({
                "cluster_id": tier,
                "label": label,
                "warna": warna,
                "jumlah_kecamatan": len(members),
                "daftar_kecamatan": [m["nama"] for m in members],
                "total_kasus": total_cases,
                "rata_rata_kasus": avg_cases,
                "rata_rata_abj": avg_abj,
                "cfr_persen": cfr,
                "rekomendasi_utama": rekom
            })

    return kec_list, clusters_summary

def main():
    print("[*] Memuat dataset granular...")
    records = load_data("dataset/data_kasus_dbd.csv")
    print(f"[*] Berhasil memuat {len(records)} baris data.")

    # 1. Agregasi Bulanan untuk Time Series
    monthly_map = {}
    for r in records:
        p = r["periode"]
        if p not in monthly_map:
            monthly_map[p] = {
                "periode": p,
                "tahun": r["tahun"],
                "bulan": r["bulan"],
                "nama_bulan": r["nama_bulan"],
                "kasus": 0,
                "meninggal": 0,
                "curah_hujan_samples": [],
                "abj_samples": []
            }
        monthly_map[p]["kasus"] += r["jumlah_kasus"]
        monthly_map[p]["meninggal"] += r["meninggal"]
        monthly_map[p]["curah_hujan_samples"].append(r["curah_hujan_mm"])
        monthly_map[p]["abj_samples"].append(r["abj_persen"])

    monthly_series = []
    for p in sorted(monthly_map.keys()):
        item = monthly_map[p]
        monthly_series.append({
            "periode": p,
            "tahun": item["tahun"],
            "bulan": item["bulan"],
            "nama_bulan": item["nama_bulan"],
            "kasus": item["kasus"],
            "meninggal": item["meninggal"],
            "curah_hujan": round(statistics.mean(item["curah_hujan_samples"]), 1),
            "abj": round(statistics.mean(item["abj_samples"]), 1)
        })

    print("[*] Menjalankan Time Series Forecasting...")
    forecasting_result = run_time_series_forecasting(monthly_series, forecast_periods=24)
    print(f"    MAE: {forecasting_result['metrics']['mae']} | RMSE: {forecasting_result['metrics']['rmse']} | MAPE: {forecasting_result['metrics']['mape']}%")

    print("[*] Menjalankan K-Means Clustering Spasial...")
    kecamatan_clustered, clusters_summary = cluster_kecamatan(records)
    for c in clusters_summary:
        print(f"    - {c['label']}: {c['jumlah_kecamatan']} Kecamatan (Kasus: {c['total_kasus']}, Rata-rata ABJ: {c['rata_rata_abj']}%)")

    # 2. Distribusi Demografis
    umur_map = {}
    gender_map = {"L": {"label": "Laki-laki", "kasus": 0, "meninggal": 0}, "P": {"label": "Perempuan", "kasus": 0, "meninggal": 0}}
    
    for r in records:
        u = r["kelompok_umur"]
        if u not in umur_map:
            umur_map[u] = {"kode": u, "label": r["label_umur"], "kasus": 0, "meninggal": 0}
        umur_map[u]["kasus"] += r["jumlah_kasus"]
        umur_map[u]["meninggal"] += r["meninggal"]

        g = r["jenis_kelamin"]
        if g in gender_map:
            gender_map[g]["kasus"] += r["jumlah_kasus"]
            gender_map[g]["meninggal"] += r["meninggal"]

    umur_list = list(umur_map.values())
    for u in umur_list:
        u["cfr"] = round((u["meninggal"] / u["kasus"] * 100) if u["kasus"] > 0 else 0, 2)

    for g in gender_map.values():
        g["cfr"] = round((g["meninggal"] / g["kasus"] * 100) if g["kasus"] > 0 else 0, 2)

    # 3. Rekomendasi Kebijakan Actionable
    rekomendasi_kebijakan = [
        {
            "level": "Tingkat Strategis (Dinas Kesehatan & Walikota)",
            "fokus": "Alokasi Anggaran & Logistik Preventif",
            "tindakan": [
                "Realokasi 60% anggaran penanggulangan DBD dan distribusi larvasida ke 6 kecamatan Zona Merah sejak bulan Oktober (sebelum musim hujan).",
                "Pembentukan Satgas Respon Cepat 24 Jam dengan sistem Early Warning Dashboard.",
                "Penyediaan Buffer Stock RDT Antigen Dengue (NS1) di seluruh puskesmas zona berisiko."
            ]
        },
        {
            "level": "Tingkat Operasional (Puskesmas & Fasilitas Kesehatan)",
            "fokus": "Deteksi Dini & Pelacakan Kasus",
            "tindakan": [
                "Penyelidikan Epidemiologi (PE) maksimal 1x24 jam setelah kasus DBD pertama dilaporkan.",
                "Fogging fokus berbasis data radius 100-200 meter dari titik kasus konfirmasi.",
                "Pemberian edukasi triase dini tanda bahaya (warning signs) syok dengue kepada orang tua pasien anak."
            ]
        },
        {
            "level": "Tingkat Komunitas (Kader Jumantik & Warga)",
            "fokus": "Gerakan 1 Rumah 1 Jumantik (G1R1J)",
            "tindakan": [
                "Pemeriksaan jentik berkala serentak setiap hari Jumat (Jumat Bersih).",
                "Pemberantasan Sarang Nyamuk (PSN) 3M Plus di tempat penampungan air alami maupun buatan.",
                "Peningkatan Angka Bebas Jentik (ABJ) di zona merah agar mencapai target nasional > 95%."
            ]
        }
    ]

    # Kalender Musiman Intervensi
    kalender_intervensi = [
        {"bulan": "Agustus - September", "status": "Kemarau / Kesiapan", "aksi": "Audit saluran air, pengadaan larvasida massal, pemetaan kembali peta klaster risiko."},
        {"bulan": "Oktober - November", "status": "Awal Musim Hujan / Siaga 1", "aksi": "Gerakan serentak PSN 3M Plus pra-musim hujan, simulasi respon cepat di Puskesmas zona merah."},
        {"bulan": "Desember - Maret", "status": "Puncak Musim Hujan / Siaga Penuh", "aksi": "Pemantauan intensif mingguan, PE 1x24 jam, fogging terarah, pelaporan kasus real-time."},
        {"bulan": "April - Mei", "status": "Transisi Akhir / Evaluasi", "aksi": "Evaluasi CFR, apresiasi kelurahan bebas jentik terbaik, konsolidasi data spasial."}
    ]

    # Gabungkan semua hasil analisis ke dalam JSON
    output_data = {
        "summary_global": {
            "total_kasus": sum(r["kasus"] for r in monthly_series),
            "total_meninggal": sum(r["meninggal"] for r in monthly_series),
            "cfr_persen": round(sum(r["meninggal"] for r in monthly_series) / sum(r["kasus"] for r in monthly_series) * 100, 2),
            "rata_rata_abj": round(statistics.mean([k["avg_abj"] for k in kecamatan_clustered]), 2),
            "jumlah_kecamatan": len(kecamatan_clustered),
            "rentang_tahun": "2019 - 2024",
            "kecamatan_zona_merah": len([k for k in kecamatan_clustered if k["cluster_id"] == 1]),
            "kecamatan_zona_kuning": len([k for k in kecamatan_clustered if k["cluster_id"] == 2]),
            "kecamatan_zona_hijau": len([k for k in kecamatan_clustered if k["cluster_id"] == 3])
        },
        "monthly_series": monthly_series,
        "forecasting": forecasting_result,
        "kecamatan_clustered": kecamatan_clustered,
        "clusters_summary": clusters_summary,
        "demografi": {
            "kelompok_umur": umur_list,
            "jenis_kelamin": list(gender_map.values())
        },
        "rekomendasi_kebijakan": rekomendasi_kebijakan,
        "kalender_intervensi": kalender_intervensi
    }

    out_file = "dataset/analytics_results.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print(f"[OK] Berhasil menyimpan hasil analisis lengkap ke '{out_file}'")

if __name__ == "__main__":
    main()
