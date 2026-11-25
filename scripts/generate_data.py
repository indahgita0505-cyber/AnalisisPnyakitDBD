"""
Script: generate_data.py
Deskripsi: Menghasilkan dataset kasus DBD realistis berskala besar
berdasarkan tahun, bulan, kecamatan, umur, dan jenis kelamin,
dilengkapi variabel iklim (curah hujan, suhu, kelembaban) dan indikator kesehatan (ABJ, CFR).
"""

import csv
import json
import math
import random
from datetime import datetime

# Seed untuk reprodusibilitas
random.seed(42)

# Konfigurasi Dimensi Data
TAHUN_LIST = [2019, 2020, 2021, 2022, 2023, 2024]
BULAN_LIST = list(range(1, 13))

NAMA_BULAN = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

# 20 Kecamatan (Karakteristik Urban & Peri-Urban)
KECAMATAN_DATA = [
    {"nama": "Cicendo", "lat": -6.9034, "lng": 107.5973, "populasi": 98500, "luas_km2": 6.8, "base_risk": 1.35},
    {"nama": "Coblong", "lat": -6.8837, "lng": 107.6163, "populasi": 112000, "luas_km2": 7.4, "base_risk": 1.20},
    {"nama": "Batununggal", "lat": -6.9388, "lng": 107.6258, "populasi": 124000, "luas_km2": 5.2, "base_risk": 1.45},
    {"nama": "Kiaracondong", "lat": -6.9242, "lng": 107.6492, "populasi": 131000, "luas_km2": 6.1, "base_risk": 1.50},
    {"nama": "Lengkong", "lat": -6.9333, "lng": 107.6194, "populasi": 72000, "luas_km2": 5.9, "base_risk": 1.05},
    {"nama": "Regol", "lat": -6.9392, "lng": 107.6083, "populasi": 83000, "luas_km2": 4.3, "base_risk": 1.25},
    {"nama": "Sukajadi", "lat": -6.8856, "lng": 107.5894, "populasi": 108000, "luas_km2": 5.3, "base_risk": 1.15},
    {"nama": "Sukasari", "lat": -6.8672, "lng": 107.5833, "populasi": 84000, "luas_km2": 6.3, "base_risk": 0.90},
    {"nama": "Bojongloa Kaler", "lat": -6.9292, "lng": 107.5878, "populasi": 126000, "luas_km2": 3.8, "base_risk": 1.55},
    {"nama": "Bojongloa Kidul", "lat": -6.9506, "lng": 107.5956, "populasi": 89000, "luas_km2": 6.2, "base_risk": 1.20},
    {"nama": "Astanaanyar", "lat": -6.9344, "lng": 107.5989, "populasi": 71000, "luas_km2": 2.9, "base_risk": 1.30},
    {"nama": "Babakan Ciparay", "lat": -6.9389, "lng": 107.5764, "populasi": 145000, "luas_km2": 7.5, "base_risk": 1.40},
    {"nama": "Bandung Kulon", "lat": -6.9186, "lng": 107.5678, "populasi": 139000, "luas_km2": 6.5, "base_risk": 1.35},
    {"nama": "Bandung Wetan", "lat": -6.9069, "lng": 107.6169, "populasi": 31000, "luas_km2": 3.4, "base_risk": 0.65},
    {"nama": "Sumur Bandung", "lat": -6.9175, "lng": 107.6128, "populasi": 37000, "luas_km2": 3.4, "base_risk": 0.70},
    {"nama": "Cibeunying Kaler", "lat": -6.8928, "lng": 107.6339, "populasi": 70000, "luas_km2": 4.5, "base_risk": 0.85},
    {"nama": "Cibeunying Kidul", "lat": -6.9056, "lng": 107.6433, "populasi": 115000, "luas_km2": 5.3, "base_risk": 1.10},
    {"nama": "Antapani", "lat": -6.9167, "lng": 107.6617, "populasi": 79000, "luas_km2": 4.0, "base_risk": 0.95},
    {"nama": "Arcamanik", "lat": -6.9139, "lng": 107.6806, "populasi": 78000, "luas_km2": 6.1, "base_risk": 0.80},
    {"nama": "Ujungberung", "lat": -6.9142, "lng": 107.7014, "populasi": 88000, "luas_km2": 6.4, "base_risk": 0.75}
]

KELOMPOK_UMUR = [
    {"kode": "<5 thn", "label": "Balita (<5 thn)", "bobot": 0.18, "cfr_multiplier": 1.8},
    {"kode": "5-14 thn", "label": "Anak-anak (5-14 thn)", "bobot": 0.42, "cfr_multiplier": 1.4},
    {"kode": "15-44 thn", "label": "Dewasa Produktif (15-44 thn)", "bobot": 0.28, "cfr_multiplier": 0.7},
    {"kode": ">44 thn", "label": "Lansia (>44 thn)", "bobot": 0.12, "cfr_multiplier": 2.2}
]

JENIS_KELAMIN = [
    {"kode": "L", "label": "Laki-laki", "bobot": 0.52},
    {"kode": "P", "label": "Perempuan", "bobot": 0.48}
]

def get_climate_data(bulan, tahun):
    """
    Simulasi data cuaca tropis berdasarkan siklus musiman Indonesia:
    Puncak hujan: Desember - Maret
    Transisi: April - Mei, Oktober - November
    Kemarau: Juni - September
    Ada variasi El Nino (2019 kering, 2023 kering) dan La Nina (2021-2022 basah).
    """
    seasonal_factors = {
        1: {"rain": 310, "humid": 86, "temp": 26.2},
        2: {"rain": 290, "humid": 85, "temp": 26.4},
        3: {"rain": 270, "humid": 84, "temp": 26.8},
        4: {"rain": 210, "humid": 82, "temp": 27.2},
        5: {"rain": 140, "humid": 80, "temp": 27.5},
        6: {"rain": 85,  "humid": 77, "temp": 27.2},
        7: {"rain": 60,  "humid": 74, "temp": 26.9},
        8: {"rain": 55,  "humid": 73, "temp": 27.4},
        9: {"rain": 90,  "humid": 75, "temp": 28.1},
        10: {"rain": 180, "humid": 79, "temp": 27.9},
        11: {"rain": 260, "humid": 83, "temp": 27.1},
        12: {"rain": 330, "humid": 87, "temp": 26.3}
    }
    
    # Anomali tahunan
    year_anomaly = 1.0
    if tahun in [2021, 2022]: # La Nina (curah hujan lebih tinggi)
        year_anomaly = 1.22
    elif tahun in [2019, 2023]: # El Nino (lebih kering)
        year_anomaly = 0.85
        
    base = seasonal_factors[bulan]
    rain = round(base["rain"] * year_anomaly + random.uniform(-25, 25), 1)
    rain = max(15.0, rain)
    humid = round(base["humid"] + random.uniform(-2.5, 2.5), 1)
    temp = round(base["temp"] + random.uniform(-0.6, 0.6), 1)
    
    return rain, humid, temp

def main():
    rows = []
    summary_by_month_kec = []
    
    row_id = 1
    
    for tahun in TAHUN_LIST:
        for bulan in BULAN_LIST:
            rain, humid, temp = get_climate_data(bulan, tahun)
            
            # Faktor transmisi vektor DBD (nyamuk Aedes aegypti suka genangan hujan dan kelembapan tinggi)
            # Siklus DBD biasanya memuncak 1 bulan setelah awal musim hujan (lag time)
            rain_factor = (rain / 200.0) ** 1.15
            humid_factor = (humid / 80.0) ** 1.1
            
            # Siklus tahunan 3-4 tahunan wabah DBD di Indonesia
            outbreak_year_multiplier = 1.0
            if tahun == 2020:
                outbreak_year_multiplier = 0.85 # Pandemi lockdown/underreporting
            elif tahun == 2022:
                outbreak_year_multiplier = 1.35 # Rebound pasca-pandemi
            elif tahun == 2024:
                outbreak_year_multiplier = 1.45 # Lonjakan kasus 2024 nasional
                
            for kec in KECAMATAN_DATA:
                kepadatan = round(kec["populasi"] / kec["luas_km2"], 1)
                density_factor = 0.8 + (kepadatan / 15000.0) * 0.4
                
                # Angka Bebas Jentik (ABJ) normal target Kemenkes > 95%
                # Wilayah risiko tinggi memiliki ABJ rendah (82% - 90%)
                base_abj = 94.0 - (kec["base_risk"] - 0.7) * 9.0 + random.uniform(-2.5, 2.5)
                abj = max(78.0, min(97.5, round(base_abj, 1)))
                abj_risk_factor = max(0.6, (98.0 - abj) / 10.0)
                
                # Menghitung estimasi total kasus bulanan untuk kecamatan ini
                expected_monthly_cases = (
                    14.0 
                    * kec["base_risk"] 
                    * rain_factor 
                    * humid_factor 
                    * density_factor 
                    * abj_risk_factor 
                    * outbreak_year_multiplier
                )
                
                # Tambahkan noise Poisson-like
                kec_total_cases = max(0, int(round(expected_monthly_cases + random.gauss(0, math.sqrt(expected_monthly_cases)))))
                
                # Simpan agregasi per kecamatan per bulan
                summary_by_month_kec.append({
                    "tahun": tahun,
                    "bulan": bulan,
                    "nama_bulan": NAMA_BULAN[bulan - 1],
                    "periode": f"{tahun}-{bulan:02d}",
                    "kecamatan": kec["nama"],
                    "lat": kec["lat"],
                    "lng": kec["lng"],
                    "populasi": kec["populasi"],
                    "kepadatan": kepadatan,
                    "abj": abj,
                    "curah_hujan_mm": rain,
                    "kelembaban_persen": humid,
                    "suhu_c": temp,
                    "total_kasus": kec_total_cases
                })
                
                # Bagi kasus ke demografi (umur & gender)
                for umur in KELOMPOK_UMUR:
                    for gender in JENIS_KELAMIN:
                        cell_share = umur["bobot"] * gender["bobot"]
                        expected_cell = kec_total_cases * cell_share
                        
                        # Kasus integer
                        cell_cases = max(0, int(round(expected_cell + random.uniform(-0.4, 0.4))))
                        
                        # Kasus Sembuh & Meninggal (CFR rata-rata DBD Indonesia ~ 0.5% - 1.2%, lebih tinggi di balita & lansia)
                        base_cfr = 0.0075 * umur["cfr_multiplier"]
                        meninggal = 0
                        if cell_cases > 0:
                            # Peluang ada kematian
                            for _ in range(cell_cases):
                                if random.random() < base_cfr:
                                    meninggal += 1
                        
                        sembuh = cell_cases - meninggal
                        
                        rows.append({
                            "id": row_id,
                            "tahun": tahun,
                            "bulan": bulan,
                            "nama_bulan": NAMA_BULAN[bulan - 1],
                            "periode": f"{tahun}-{bulan:02d}",
                            "kecamatan": kec["nama"],
                            "lat": kec["lat"],
                            "lng": kec["lng"],
                            "kelompok_umur": umur["kode"],
                            "label_umur": umur["label"],
                            "jenis_kelamin": gender["kode"],
                            "jumlah_kasus": cell_cases,
                            "sembuh": sembuh,
                            "meninggal": meninggal,
                            "curah_hujan_mm": rain,
                            "kelembaban_persen": humid,
                            "suhu_c": temp,
                            "abj_persen": abj,
                            "kepadatan_penduduk": kepadatan
                        })
                        row_id += 1

    # Tulis CSV Granular
    csv_filename = "dataset/data_kasus_dbd.csv"
    fieldnames = [
        "id", "tahun", "bulan", "nama_bulan", "periode", "kecamatan", 
        "lat", "lng", "kelompok_umur", "label_umur", "jenis_kelamin", 
        "jumlah_kasus", "sembuh", "meninggal", "curah_hujan_mm", 
        "kelembaban_persen", "suhu_c", "abj_persen", "kepadatan_penduduk"
    ]
    
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"[OK] Berhasil menghasilkan {len(rows)} baris data granular di '{csv_filename}'")
    
    # Hitung total kasus keseluruhan
    total_kasus_all = sum(r["jumlah_kasus"] for r in rows)
    total_mati_all = sum(r["meninggal"] for r in rows)
    cfr_overall = round((total_mati_all / total_kasus_all * 100) if total_kasus_all > 0 else 0, 2)
    
    print(f"Total Kasus: {total_kasus_all:,} | Total Meninggal: {total_mati_all} | CFR: {cfr_overall}%")
    
    # Tulis file summary JSON untuk mempermudah dashboard web
    summary_data = {
        "metadata": {
            "judul": "Dataset Kasus DBD Terintegrasi",
            "cakupan": "20 Kecamatan Wilayah Urban",
            "rentang_tahun": f"{TAHUN_LIST[0]} - {TAHUN_LIST[-1]}",
            "total_records": len(rows),
            "total_kasus": total_kasus_all,
            "total_meninggal": total_mati_all,
            "cfr_persen": cfr_overall,
            "kecamatan_list": [k["nama"] for k in KECAMATAN_DATA],
            "koordinat_kecamatan": {k["nama"]: {"lat": k["lat"], "lng": k["lng"], "populasi": k["populasi"]} for k in KECAMATAN_DATA}
        }
    }
    
    with open("dataset/data_dbd_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)
        
    print("[OK] Metadata summary disimpan di 'dataset/data_dbd_summary.json'")

if __name__ == "__main__":
    main()
