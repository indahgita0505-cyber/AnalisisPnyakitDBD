# Kamus Data & Dokumentasi Sumber Dataset DBD

## 1. Identitas Dataset
* **Judul Dataset**: Dataset Longitudinal Kasus Demam Berdarah Dengue (DBD) Perkotaan
* **Cakupan Wilayah**: 20 Kecamatan (Wilayah Metropolitan / Urban Cluster)
* **Periode Waktu**: 2019 – 2024 (72 Bulan / 6 Tahun Penuh)
* **Jumlah Record**: 11.520 Baris Data Terstruktur Granular
* **Total Kasus Terdata**: 30.046 Kasus Konfirmasi
* **Total Kematian Terdata**: 322 Kasus Kematian (Case Fatality Rate: 1.07%)
* **Format Berkas**: Comma-Separated Values (`data_kasus_dbd.csv`) & JSON Format (`analytics_results.json`)

---

## 2. Sumber & Rujukan Data (Data Provenance)
Data ini dikompilasi dan dimodelkan secara realistis berdasarkan referensi statistik resmi penanggulangan DBD di Indonesia:
1. **Kementerian Kesehatan Republik Indonesia (Kemenkes RI)**:
   - *Profil Kesehatan Indonesia 2020 - 2023*, Subdit Penyakit Tular Vektor dan Zoonotik.
   - Indikator Nasional Angka Bebas Jentik (ABJ target nasional $\ge 95\%$) dan batas toleransi Case Fatality Rate (CFR target $< 1\%$).
2. **Badan Pusat Statistik (BPS)**:
   - Data Agregat Kependudukan dan Luas Wilayah Kecamatan Wilayah Perkotaan (Metrik Kepadatan Jiwa/$\text{km}^2$).
3. **Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)**:
   - Pola Historis Curah Hujan Bulanan (mm), Kelembaban Relatif (%), dan Suhu Udara Rata-rata (°C) di Pulau Jawa.
4. **Portal Satu Data Indonesia & Open Data Jabar / Jakarta**:
   - Struktur sebaran spasial dan stratifikasi kasus DBD berdasarkan kelompok umur dan jenis kelamin.

---

## 3. Kamus Variabel (Data Dictionary)

| Nama Kolom | Tipe Data | Satuan / Nilai | Deskripsi Variabel |
| :--- | :--- | :--- | :--- |
| `id` | Integer | 1, 2, 3, ... | Identifikator unik untuk setiap baris data transaksi. |
| `tahun` | Integer | 2019 – 2024 | Tahun pencatatan data surveilans epidemiologi. |
| `bulan` | Integer | 1 – 12 | Angka bulan pencatatan kasus (1 = Januari, ..., 12 = Desember). |
| `nama_bulan` | String | Januari – Desember | Nama bulan pencatatan dalam Bahasa Indonesia. |
| `periode` | String | `YYYY-MM` | Format standar representasi deret waktu bulanan (contoh: `2024-03`). |
| `kecamatan` | String | Nama Kecamatan | Nama wilayah administratif tingkat kecamatan tempat domisili pasien. |
| `lat` | Float | Derajat Desimal | Koordinat lintang (Latitude) pusat aktivitas/puskesmas kecamatan. |
| `lng` | Float | Derajat Desimal | Koordinat bujur (Longitude) pusat aktivitas/puskesmas kecamatan. |
| `kelompok_umur` | String | `<5 thn`, `5-14 thn`, `15-44 thn`, `>44 thn` | Kategori stratifikasi umur pasien sesuai standar WHO & Kemenkes. |
| `label_umur` | String | Balita, Anak-anak, Dewasa Produktif, Lansia | Label deskriptif kelompok umur. |
| `jenis_kelamin` | String | `L`, `P` | Jenis kelamin pasien (`L` = Laki-laki, `P` = Perempuan). |
| `jumlah_kasus` | Integer | Pasien | Jumlah pasien yang terdiagnosis positif DBD (NS1 / IgG / IgM Dengue). |
| `sembuh` | Integer | Pasien | Jumlah pasien DBD yang dinyatakan sembuh setelah perawatan. |
| `meninggal` | Integer | Pasien | Jumlah kematian akibat syok atau komplikasi dengue (DHF/DSS). |
| `curah_hujan_mm` | Float | Milimeter (mm) | Akumulasi curah hujan bulanan di stasiun pengamatan BMKG setempat. |
| `kelembaban_persen` | Float | Persen (%) | Rata-rata kelembaban udara relatif harian dalam bulan berjalan. |
| `suhu_c` | Float | Derajat Celcius (°C) | Rata-rata suhu udara bulanan di wilayah pengamatan. |
| `abj_persen` | Float | Persen (%) | **Angka Bebas Jentik**: Persentase rumah/tempat yang diperiksa tidak ditemukan jentik nyamuk Aedes aegypti (Target ideal $\ge 95\%$). |
| `kepadatan_penduduk` | Float | Jiwa per $\text{km}^2$ | Kepadatan demografi kecamatan (Populasi / Luas Wilayah). |

---

## 4. Struktur Klaster Risiko Wilayah (Hasil K-Means)
Berdasarkan analisis klaster multivariat (Total Kasus, Defisit ABJ, dan Kepadatan Penduduk):
* **Cluster 1 (Zona Merah / High Risk)**:
  - Karakteristik: Rata-rata kasus tinggi (>2.500 kasus/wilayah), ABJ rendah (<88%), pemukiman padat.
  - Aksi: Prioritas 1 — Fogging fokus radius 100m, larvasida massal, pemantauan Jumantik mingguan.
* **Cluster 2 (Zona Kuning / Moderate Risk)**:
  - Karakteristik: Rata-rata kasus moderat (~1.400 kasus/wilayah), ABJ sedang (88% - 92%).
  - Aksi: Prioritas 2 — Gerakan 3M Plus, edukasi sekolah, penertiban tempat penampungan air terbuka.
* **Cluster 3 (Zona Hijau / Low Risk)**:
  - Karakteristik: Rata-rata kasus rendah (<700 kasus/wilayah), ABJ tinggi (>93%).
  - Aksi: Prioritas 3 — Pemeliharaan lingkungan mandiri, monitoring berkala, desa percontohan.
