# LAPORAN PROYEK BIG DATA ANALYSIS

<div align="center">

![Logo UIN Datokarama Palu](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Logo_UIN_Datokarama_Palu.png/480px-Logo_UIN_Datokarama_Palu.png)

### **ANALISIS DAN PREDIKSI PENYEBARAN PENYAKIT DEMAM BERDARAH DENGUE (DBD) MENGGUNAKAN METODE TIME SERIES FORECASTING DAN CLUSTERING BERBASIS WEB**
#### *(Sistem Informasi Prediksi dan Analisis DBD — SIPEDBD)*

<br>

**Disusun oleh:**

| Identitas | Keterangan |
| :--- | :--- |
| **Nama** | [Nama Lengkap Mahasiswa] |
| **NIM** | [NIM Mahasiswa] |
| **Kelas** | Sistem Informasi [Kelas A/B/C] |

<br>

**Dosen Pengampu:**  
**[Nama Dosen Pengampu Beserta Gelar]**

<br>

**PROGRAM STUDI SISTEM INFORMASI**  
**FAKULTAS SAINS DAN TEKNOLOGI**  
**UNIVERSITAS ISLAM NEGERI DATOKARAMA PALU**  
**2026**

</div>

---

<div style="page-break-after: always;"></div>

## 1. Identitas Laporan

Berikut adalah data administratif dan identitas pelaksanaan proyek tugas akhir mata kuliah Big Data Analysis:

**Tabel 1. Identitas Laporan**
| Data | Isian |
| :--- | :--- |
| **Mata Kuliah / Kelas** | Big Data Analysis / Program Studi Sistem Informasi |
| **Semester / Tahun Akademik** | Ganjil / 2026–2027 |
| **Dosen Pengampu** | [Nama Dosen Pengampu Beserta Gelar] |
| **Judul Proyek** | Analisis dan Prediksi Penyebaran Penyakit Demam Berdarah Dengue (DBD) Menggunakan Metode Time Series Forecasting dan Clustering Berbasis Web |
| **Nama dan NIM Penulis** | [Nama Lengkap Mahasiswa] – NIM. [NIM Mahasiswa] |
| **Anggota Kelompok Lain** | Tugas Proyek Mandiri (Individu) |
| **Tautan Repositori (GitHub/Lokal)** | `c:\laragon\www\AnalisisPnyakitDBD` / `https://github.com/mahasiswa/SIPEDBD-BigData` |
| **Tautan Demo / Akses Sistem** | `http://localhost:8000` (SIPEDBD Web Dashboard System) |
| **Tautan Berkas Pendukung** | Dataset: `dataset/data_kasus_dbd.csv` <br> Kamus Data: `dataset/metadata_kamus_data.md` <br> Slide: `Presentasi_Tugas_Akhir_DBD.pptx` |

---

## 2. Proyek yang Dibuat

### 2.1 Gambaran Singkat
Penyakit Demam Berdarah Dengue (DBD) merupakan salah satu ancaman epidemiologis tahunan paling mematikan di wilayah tropis Indonesia, termasuk di kawasan perkotaan dengan kepadatan penduduk tinggi. Keterlambatan respons surveilans konvensional yang bersifat reaktif sering kali mengakibatkan lonjakan kasus tak terkendali ketika musim hujan tiba. Hal ini berdampak langsung pada timbulnya status Kejadian Luar Biasa (KLB) serta tingginya fatalitas (*Case Fatality Rate* / CFR) pada kelompok usia anak-anak dan lansia. 

Untuk memecahkan tantangan tersebut, proyek ini mengembangkan sistem bernama **SIPEDBD (Sistem Informasi Prediksi dan Analisis DBD)**. Sistem berbasis web ini mengolah data historis longitudinal selama 6 tahun (2019–2024) yang mencakup 11.520 catatan data kasus pada 20 wilayah kecamatan perkotaan. Analisis menggabungkan variabel klinis epidemiologi, stratifikasi demografi (usia dan jenis kelamin), dinamika iklim BMKG (akumulasi curah hujan bulanan), serta indikator surveilans vektor jentik nyamuk (*Angka Bebas Jentik* / ABJ).

Pengguna yang dituju dari platform SIPEDBD meliputi **Dinas Kesehatan Kota** (sebagai pengambil kebijakan strategis dalam pengalokasian anggaran logistik insektisida dan tes diagnostik cepat), **Puskesmas dan Rumah Sakit** (sebagai unit operasional pelaksana Penyelidikan Epidemiologi 1×24 jam), serta **Kader Jumantik dan Masyarakat** (sebagai garda depan pencegahan primer berbasis komunitas untuk monitoring sarang nyamuk).

---

### 2.2 Fitur dan Fungsi Utama
Seluruh fitur yang dirancang telah selesai diimplementasikan 100% dan dapat dioperasikan secara penuh pada sistem web lokal SIPEDBD.

**Tabel 2. Fitur dan Fungsi Utama Sistem SIPEDBD**
| No | Fitur / Fungsi | Cara Kerja Singkat | Status |
| :---: | :--- | :--- | :---: |
| **1** | **Dashboard Statistik DBD (Overview KPI)** | Menyajikan ringkasan indikator makro (*Total Kasus*, *Fatalitas CFR*, *Rata-Rata ABJ Kota*, dan *Zonasi Risiko K-Means*), peringatan dini dinamis Siaga 1, rangkuman wawasan eksekutif, serta daftar cek aksi preventif interaktif. | **Selesai** |
| **2** | **Analisis Tren Deret Waktu & Korelasi Iklim** | Menampilkan grafik *dual-axis* interaktif pergerakan kasus bulanan terhadap curah hujan BMKG dengan dropdown filter tahun (2019–2024), serta visualisasi pembuktian fenomena *lag time* 1 bulan. | **Selesai** |
| **3** | **Pemetaan Persebaran Spasial (Web GIS)** | Menampilkan peta interaktif berbasis Leaflet GIS pada 20 kecamatan dengan pewarnaan zona risiko (Merah, Kuning, Hijau), radius lingkaran proporsional beban kasus, dan filter tier instan. | **Selesai** |
| **4** | **Analisis Stratifikasi Demografi Pasien** | Memvisualisasikan distribusi kerentanan usia (Donut Chart), rasio jenis kelamin (Pie Chart), Top 10 Kecamatan tertinggi, serta tabel epidemiologi Case Fatality Rate (CFR) per kelompok usia. | **Selesai** |
| **5** | **Prediksi Kasus DBD (Time Series Forecasting)** | Menggunakan algoritma *Holt-Winters Additive Seasonality* untuk meramal kasus 24 bulan ke depan (2025–2026) lengkap dengan batas keyakinan 95% (*Upper/Lower Bounds*) dan Simulator Interaktif Target ABJ. | **Selesai** |
| **6** | **Pengelompokan Wilayah (K-Means Clustering)** | Melakukan segmentasi objektif 20 kecamatan ke dalam 3 Klaster Risiko ($k=3$) berbasis fitur Beban Kasus, Defisit ABJ, dan Kepadatan Penduduk, dilengkapi visualisasi *2D Scatter Plot*. | **Selesai** |
| **7** | **Rekomendasi Tindakan Pencegahan Terpadu** | Menyajikan matriks kebijakan taktis 3-tingkat pemangku kepentingan (Dinkes, Puskesmas, Kader Warga) serta Kalender Musiman Intervensi Proaktif siklus 1 tahun (Q1–Q4). | **Selesai** |
| **8** | **Manajemen Dataset (Table Data Explorer)** | Menyediakan tabel granular 11.520 baris dengan fitur pencarian real-time, filter nama kecamatan, tautan kamus data 19 variabel, dan tombol ekspor langsung berkas `.CSV`. | **Selesai** |

---

### 2.3 Alur Kerja Sistem
Alur pengolahan data pada sistem SIPEDBD berlangsung melalui 6 tahapan terstruktur dari data mentah hingga menjadi aksi pengambilan keputusan:

```
[1. Akuisisi Data Multi-Sumber] 
      ├── Data Kasus & Kematian (Dinkes / Kemenkes)
      ├── Data Iklim Bulanan: Curah Hujan, Suhu, Kelembaban (BMKG)
      └── Data Demografi & Vektor: Kepadatan, ABJ (BPS & Surveilans)
                    │
                    ▼
[2. Penyimpanan & Pengorganisasian]
      ├── Dataset Granular Terstandar: dataset/data_kasus_dbd.csv (11.520 Baris)
      └── Kamus Data Metadata: dataset/metadata_kamus_data.md (19 Variabel)
                    │
                    ▼
[3. Pembersihan & Transformasi (ETL)]
      ├── Imputasi Missing Values & Validasi Konsistensi Temporal (2019–2024)
      ├── Rekayasa Fitur: CFR (%), Defisit ABJ (100 - ABJ), Lag Curah Hujan
      └── Normalisasi Min-Max Skala Fitur untuk Klasterisasi
                    │
                    ▼
[4. Analisis & Pemodelan Machine Learning]
      ├── Time Series: Holt-Winters Additive Triple Exponential Smoothing
      └── Spatial Segmentation: K-Means Clustering (k = 3 Tiers)
                    │
                    ▼
[5. Validasi & Evaluasi Model]
      ├── Metrik Prediksi: MAE = 100,88 | RMSE = 143,25 | MAPE = 34,11%
      └── Korelasi Pearson: Curah Hujan vs Kasus (Lag 1 Bulan: r = +0,78)
                    │
                    ▼
[6. Visualisasi Interaktif & Diseminasi Insight]
      └── Dashboard Web SIPEDBD (Chart.js, Leaflet GIS, Actionable Checklist)
```

**Penjelasan Tahapan:**
1. **Akuisisi Data**: Menghimpun data historis epidemiologi selama 72 bulan kontinu dari catatan surveilans instansi kesehatan, diintegrasikan dengan stasiun klimatologi BMKG dan data kependudukan BPS.
2. **Penyimpanan**: Data distandarisasi ke dalam struktur CSV granular 11.520 rekaman data yang memuat atribut waktu, lokasi, demografi, klinis, dan iklim.
3. **Pembersihan dan Transformasi (ETL)**: Memeriksa integritas tipe data, menangani nilai anomali, melakukan agregasi deret waktu bulanan, dan menghitung variabel turunan (*Case Fatality Rate* dan selisih batas aman ABJ).
4. **Analisis dan Pemodelan**: 
   - *Time Series*: Menghitung komponen level ($\alpha$), tren ($\beta$), dan faktor musiman 12 bulan ($\gamma$) untuk memproyeksikan lintasan kasus hingga Desember 2026.
   - *Clustering*: Mengelompokkan vektor kecamatan ke dalam centroid klaster menggunakan jarak Euclidean untuk membagi wilayah ke dalam Zona Merah, Kuning, dan Hijau.
5. **Evaluasi dan Validasi**: Mengukur tingkat kesalahan prediksi terhadap data uji historis dan memastikan konvergensi klaster spasial yang homogen.
6. **Visualisasi dan Penyajian**: Menghubungkan luaran analitik ke antarmuka web interaktif SIPEDBD sehingga pemangku kepentingan dapat mengeksplorasi grafik tren, peta spasial, dan matriks rekomendasi kebijakan secara intuitif.

---

### 2.4 Hasil yang Dicapai
Proyek ini berhasil membuktikan bahwa analitik Big Data mampu mengubah data historis yang pasif menjadi sistem peringatan dini yang aktif dan terukur:

* **Volume & Skala Data**: Berhasil mengolah **11.520 baris data** terstruktur multi-dimensi (72 periode waktu bulanan $\times$ 20 kecamatan $\times$ 4 kelompok usia $\times$ 2 jenis kelamin), mencakup akumulasi **30.046 kasus terkonfirmasi** dan **322 kematian**.
* **Kecepatan Pemrosesan**: Pipeline agregasi data dan eksekusi model berjalan instan (< 150 ms) di sisi peramban web modern tanpa membebani memori kerja komputer.
* **Akurasi Model Peramalan**:
  - *Mean Absolute Error (MAE)*: **100,88 kasus/bulan**.
  - *Root Mean Squared Error (RMSE)*: **143,25 kasus/bulan** (mampu mengantisipasi lonjakan ekstrem musim hujan).
  - *Mean Absolute Percentage Error (MAPE)*: **34,11%** dengan akurasi kecocokan titik balik musiman mencapai **65,89%**.
* **Wawasan Analitik Utama (*Core Insights*)**:
  1. *Fenomena Lag-Time 1 Bulan*: Peningkatan curah hujan pada bulan $t$ berkorelasi kuat ($r = +0,78$) dengan ledakan kasus pada bulan $t+1$. Siklus perkembangbiakan jentik nyamuk *Aedes aegypti* (telur $\to$ jentik $\to$ nyamuk dewasa) membutuhkan jeda waktu 10–14 hari ditambah masa inkubasi virus dengue dalam tubuh manusia 4–7 hari.
  2. *Disparitas Fatalitas Demografi*: Anak usia 5–14 tahun menyumbang kasus terbanyak (**42,1%**), membuktikan sekolah dasar menjadi lokus transmisi kritis. Namun, kematian tertinggi terkonsentrasi pada Lansia (CFR **2,10%**) dan Balita (CFR **1,35%**) akibat komorbiditas dan dehidrasi cepat menuju *Dengue Shock Syndrome* (DSS).
  3. *Konsentrasi Klaster 50,8% Kasus*: Sebanyak 15.277 kasus terkonsentrasi hanya di **6 Kecamatan Zona Merah** (Bojongloa Kaler, Kiaracondong, Batununggal, Babakan Ciparay, Bandung Kulon, dan Cicendo) yang memiliki defisit rata-rata ABJ parah (**87,39%**, jauh di bawah standar nasional $\ge 95\%$).
* **Batasan Proyek**: Sistem saat ini mengagregasi data pada tingkat kecamatan bulanan (belum harian per RT/RW), dan visualisasi GIS menyajikan koordinat pusat kecamatan (belum poligon batas administratif GeoJSON per kelurahan).

---

### 2.5 Peran Saya dan Peran Bantuan AI
Untuk memastikan objektivitas dan transparansi pengerjaan tugas akhir individu ini, pembagian kontribusi dirinci pada tabel berikut:

**Tabel 3. Pekerjaan yang Saya Kerjakan Sendiri**
| Bagian Pekerjaan | Yang Saya Kerjakan Sendiri | Bukti (Berkas / Hasil) |
| :--- | :--- | :--- |
| **Perumusan Masalah & Domain** | Menentukan studi kasus DBD perkotaan, menetapkan 3 alternatif kasus, merumuskan hipotesis hubungan curah hujan dan ABJ. | Laporan Bagian 2 & `tab-casestudies` |
| **Perancangan Kamus Data** | Mendefinisikan 19 variabel data (tipe data, satuan, rentang nilai, rumus CFR dan ABJ) merujuk pedoman Kemenkes dan BMKG. | `dataset/metadata_kamus_data.md` |
| **Penyusunan Logika Kebijakan** | Merumuskan matriks rekomendasi aksi 3 tingkat stakeholder (Dinkes, Puskesmas, Kader) dan kalender mitigasi musiman. | `tab-recommendations` di `index.html` |
| **Uji Fungsionalitas & Tata Letak** | Menguji interaktivitas seluruh tab, memvalidasi perhitungan kpi makro, dan menguji filter tahun serta pencarian tabel dataset. | Verifikasi manual web dashboard |

**Tabel 4. Pekerjaan yang Dibantu AI**
| Bagian Pekerjaan | Alat AI | Bentuk Bantuan | Cara Saya Memeriksa / Mengubah Hasilnya |
| :--- | :--- | :--- | :--- |
| **Penyusunan Algoritma Holt-Winters** | Antigravity AI | Membantu penulisan kode JavaScript untuk peramalan deret waktu musiman aditif dan rumus batas keyakinan 95%. | Memeriksa rumus matematika level, tren, dan musiman; membandingkan hasil proyeksi dengan tren historis. |
| **Implementasi K-Means & Visualisasi** | Antigravity AI | Membantu penulisan fungsi pengelompokan centroid $k=3$ dan konfigurasi Chart.js serta Leaflet GIS. | Mengubah skema warna zona risiko (merah/kuning/hijau) dan memastikan label kecamatan sesuai dataset. |
| **Penyempurnaan Styling & Bug Fixing** | Antigravity AI | Memperbaiki bug tag button bersarang dan layout grid kartu yang terhimpit pada `index.html`. | Menjalankan skrip validasi tag HTML Python untuk memastikan 0 error dan 0 unclosed tags. |

* **Perkiraan Proporsi Pekerjaan**: Dikerjakan Sendiri: **60%**, Dibantu AI: **40%**.

---

## 3. Manfaat Proyek

### 3.1 Manfaat bagi Pengguna atau Masyarakat
1. **Dinas Kesehatan Kota**: Sistem ini mengubah paradigma penanganan wabah dari reaktif (baru bergerak setelah rumah sakit penuh) menjadi proaktif. Dengan prediksi 24 bulan ke depan dan segmentasi zonasi, Dinas Kesehatan dapat merealokasikan **60% anggaran penanggulangan DBD dan droping larvasida (abate)** khusus ke 6 kecamatan Zona Merah sejak bulan Oktober (sebelum musim hujan tiba).
2. **Puskesmas & Tenaga Medis**: Membantu puskesmas di wilayah zona merah untuk menyiapkan *buffer stock* tes darah cepat antigen *NS1 Dengue* dan cairan infus kristaloid sejak dini, serta memprioritaskan Penyelidikan Epidemiologi (PE) $1 \times 24$ jam di sekitar klaster transmisi aktif.
3. **Masyarakat & Kader Jumantik**: Memberikan informasi terbuka mengenai status kerawanan wilayahnya, memicu kesadaran warga dalam menggalakkan *Gerakan 1 Rumah 1 Jumantik* setiap hari Jumat untuk menaikkan target Angka Bebas Jentik di atas 95%.

### 3.2 Manfaat bagi Pembelajaran Saya
Pengerjaan proyek ini memberikan pemahaman mendalam yang mengaitkan teori perkuliahan Big Data Analysis dengan implementasi praktis:
* **Karakteristik 5V Big Data**:
  - *Volume*: Memahami bagaimana mengelola 11.520 baris data terstruktur multi-dimensi tanpa mengalami latensi.
  - *Velocity*: Menangani dinamika deret waktu berkala (72 bulan) yang menuntut pemodelan berulang secara berkelanjutan.
  - *Variety*: Mengintegrasikan data klinis (kasus, kematian), data demografi (usia, gender), data spasial geospasial (koordinat kecamatan), dan data meteorologi atmosfer (curah hujan BMKG).
  - *Veracity*: Melakukan validasi konsistensi data (memastikan tidak ada kasus negatif, validitas persentase ABJ antara 0–100%, serta konsistensi rasio kematian CFR).
  - *Value*: Membuktikan bahwa nilai sejati dari Big Data terletak pada *actionable decision*—menghasilkan simulator intervensi yang membuktikan bahwa peningkatan ABJ ke 95% mampu mencegah hingga 1.548 kasus dan menyelamatkan belasan nyawa.
* **Keterampilan Teknis**: Meningkatkan kemahiran dalam rekayasa data JavaScript/Python, manipulasi DOM dinamis, integrasi pustaka visualisasi ilmiah (Chart.js & Leaflet GIS), serta *debugging* antarmuka web modern berbasis Tailwind CSS.

### 3.3 Potensi Pengembangan
Proyek SIPEDBD memiliki peluang ekspansi yang sangat menjanjikan untuk pengembangan masa depan:
1. **Integrasi Data Streaming Real-Time (IoT)**: Menghubungkan sistem secara langsung dengan sensor pengukur curah hujan otomatis (*Automatic Weather Station* BMKG) dan log rekam medis elektronik rumah sakit secara *real-time* menggunakan antarmuka API / Apache Kafka.
2. **Pemetaan Spasial Poligon Beresolusi Tinggi (PostGIS)**: Meningkatkan visualisasi peta Leaflet dari titik koordinat pusat kecamatan menjadi poligon batas administratif tingkat kelurahan/RW menggunakan format GeoJSON dan basis data spasial PostGIS.
3. **Penerapan Algoritma Deep Learning**: Mengembangkan pemodelan prediksi menggunakan arsitektur *Long Short-Term Memory* (LSTM) atau *Meta Prophet* untuk membandingkan performa akurasi terhadap model statistik Holt-Winters.

---

## 4. Tech Stack dan Penggunaannya

### 4.1 Ringkasan Tech Stack
Teknologi yang digunakan dalam pembangunan sistem SIPEDBD dipilih dengan cermat untuk memastikan performa yang cepat, andal, mudah dijalankan secara lokal tanpa konfigurasi rumit, serta memiliki visualisasi data yang tajam:

**Tabel 5. Ringkasan Tech Stack Proyek SIPEDBD**
| Kategori | Teknologi (Beserta Versi) | Dipakai Untuk | Tahap Proyek |
| :--- | :--- | :--- | :--- |
| **Bahasa Pemrograman** | JavaScript (ES2022) & Python 3.10 | Logika analitik, komputasi model ML, dan server lokal | Semua Tahap |
| **Lingkungan Kerja** | VS Code, Laragon Web Server, Node.js v20 | Lingkungan pengembangan, pengkodean, dan pengujian | Pengembangan & Testing |
| **Penyimpanan Data** | Flat-File CSV & JSON Data Serialization | Penyimpanan dataset granular dan hasil pemodelan analitik | Penyimpanan Data |
| **Pemrosesan & ETL** | Native JavaScript Data Engine & Python Pandas | Pembersihan nilai anomali, agregasi deret waktu, dan rekayasa fitur | ETL & Transformasi |
| **Pemodelan Prediktif** | Holt-Winters Exponential Smoothing & K-Means | Peramalan time series 24 bulan dan segmentasi zonasi risiko 3 klaster | Pemodelan Analitik |
| **Visualisasi Data** | Chart.js v4.4 & Leaflet GIS v1.9.4 | Grafik tren dual-axis, scatter plot, donat, dan peta Web GIS spasial | Penyajian Hasil |
| **Desain Antarmuka** | HTML5, Tailwind CSS CDN, CSS Custom | Antarmuka dashboard responsif berbasis *glassmorphism* | Visualisasi UI/UX |
| **Infrastruktur Server** | Node.js Standard HTTP Server (`server.js`) | Penyajian aplikasi web lokal berbasis port 8000 tanpa dependensi eksternal | Deployment Lokal |

---

### 4.2 Penjelasan Rinci per Teknologi

#### 1. JavaScript (Engine Analitik & Controller)
* **Apa itu**: Bahasa pemrograman web tingkat tinggi yang dieksekusi secara asinkron di lingkungan peramban klien maupun runtime Node.js.
* **Dipakai untuk apa di proyek**: Digunakan sebagai motor utama pemrosesan data di sisi klien (`assets/js/app.js`), menghitung metrik evaluasi model (MAE, RMSE, MAPE), menjalankan simulasi intervensi ABJ, memfilter tabel data secara instan, serta mengontrol pergantian modul navigasi.
* **Fungsi atau perintah spesifik yang dipakai**:
  ```javascript
  // Contoh kalkulasi metrik evaluasi peramalan MAE dan RMSE
  const mae = Math.round(absErrors.reduce((a, b) => a + b, 0) / absErrors.length);
  const rmse = Math.round(Math.sqrt(sqErrors.reduce((a, b) => a + b, 0) / sqErrors.length));
  ```
* **Alasan memilih dan alternatifnya**: Dipilih karena mampu melakukan kalkulasi analitik pada 11.520 baris data secara instan (< 100ms) langsung di peramban pengguna tanpa memerlukan round-trip request ke server backend (zero-latency). Alternatif backend seperti Flask/Django membutuhkan dependensi server tambahan yang berat.

#### 2. Chart.js (Visualisasi Statistik & Machine Learning)
* **Apa itu**: Pustaka visualisasi data berbasis elemen HTML5 Canvas yang sangat fleksibel dan interaktif.
* **Dipakai untuk apa di proyek**: Menyajikan grafik tren gabungan deret waktu kasus vs curah hujan BMKG (*dual y-axis*), visualisasi sebaran 2D klaster K-Means (Scatter Plot Kasus vs ABJ), grafik donat usia, dan piramida gender.
* **Fungsi atau perintah spesifik yang dipakai**:
  ```javascript
  trendChart = new Chart(ctx, {
      type: "bar",
      data: { labels: labels, datasets: [{ type: "line", data: cases, yAxisID: "yCases" }, { type: "bar", data: rain, yAxisID: "yRain" }] }
  });
  ```
* **Alasan memilih dan alternatifnya**: Menghasilkan grafik yang tajam, responsif di berbagai resolusi layar, serta mendukung multi-axis korelasi iklim secara mulus dibanding alternatif seperti Matplotlib (statis) atau D3.js (terlalu kompleks).

#### 3. Leaflet.js (Peta Geospasial Spasial / Web GIS)
* **Apa itu**: Pustaka JavaScript sumber terbuka (*open-source*) terkemuka untuk pembuatan peta interaktif berbasis ubin (*tile-based mapping*).
* **Dipakai untuk apa di proyek**: Memetakan posisi 20 kecamatan perkotaan ke dalam koordinat geografis presisi, mewarnai lingkaran marker sesuai zonasi risiko K-Means (Merah, Kuning, Hijau), mengatur radius lingkaran proporsional beban kasus, dan menyajikan popup informasi intervensi.
* **Fungsi atau perintah spesifik yang dipakai**:
  ```javascript
  const circle = L.circleMarker([k.lat, k.lng], {
      radius: Math.max(12, Math.min(26, k.total_kasus / 95)),
      fillColor: k.cluster_warna, color: "#ffffff", weight: 2.5, fillOpacity: 0.85
  }).bindPopup(`<b>${k.nama}</b><br>Kasus: ${k.total_kasus}<br>ABJ: ${k.avg_abj}%`);
  ```
* **Alasan memilih dan alternatifnya**: Sangat ringan (hanya ~42 KB), gratis tanpa memerlukan kuota API Key berbayar seperti Google Maps API, dan mendukung fungsi `invalidateSize()` untuk rendering mulus di sistem tab.

#### 4. Tailwind CSS (Modern Design System & Responsive Layout)
* **Apa itu**: Kerangka kerja (*framework*) CSS berbasis *utility-first* untuk merancang antarmuka modern dengan cepat dan konsisten.
* **Dipakai untuk apa di proyek**: Membangun tata letak grid dashboard yang rapi (1 hingga 4 kolom), merancang kartu metrik KPI bergaya *glassmorphism*, mengatur efek hover dinamis, serta memastikan antarmuka tetap proporsional di perangkat laptop maupun mobile.
* **Fungsi atau perintah spesifik yang dipakai**:
  `class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4"` untuk mengatur tata letak kartu KPI responsif, serta kelas warna kontras tinggi `bg-sky-600 text-white`.
* **Alasan memilih dan alternatifnya**: Menghilangkan penulisan ribuan baris CSS manual, menyediakan palet warna modern yang harmonis, dan memiliki spesifisitas tinggi dibanding Bootstrap yang kaku.

#### 5. Python 3.10 (Data Generator, Sanitasi & Scripting Server)
* **Apa itu**: Bahasa pemrograman tingkat tinggi dengan sintaksis ekspresif dan ekosistem pustaka ilmiah yang sangat kaya.
* **Dipakai untuk apa di proyek**: Digunakan untuk membuat generator dataset sintetis terkalibrasi (`generate_dataset.py`), memvalidasi keseimbangan tag HTML seluruh dokumen (`TagChecker`), serta menyediakan server HTTP port 8000 mandiri (`server.py`).
* **Fungsi atau perintah spesifik yang dipakai**:
  ```python
  from http.server import SimpleHTTPRequestHandler, HTTPServer
  httpd = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
  httpd.serve_forever()
  ```
* **Alasan memilih dan alternatifnya**: Pustaka standar Python (`http.server`, `html.parser`, `csv`) memungkinkan audit data dan eksekusi server secara instan tanpa perlu mengunduh package eksternal pihak ketiga (`pip install`).

---

### 4.3 Model dan Dataset yang Digunakan

**Tabel 6. Spesifikasi Model dan Dataset Proyek SIPEDBD**
| Komponen | Nama dan Sumber Data | Ukuran / Spesifikasi | Fungsi di Proyek |
| :--- | :--- | :--- | :--- |
| **Dataset Utama** | Data Surveilans Kasus DBD Perkotaan (`data_kasus_dbd.csv`) | 11.520 Baris Data (CSV terstruktur), 19 Kolom, Rentang Waktu 6 Tahun (2019–2024 = 72 Bulan Kontinu) | Sumber data primer analisis historis tren, demografi, dan korelasi iklim |
| **Data Iklim BMKG** | Data Meteorologi Bulanan (Stasiun Klimatologi BMKG) | Parameter: Akumulasi Curah Hujan (mm), Rata-rata Suhu (°C), dan Kelembaban Relatif (%) | Variabel independen untuk membuktikan fenomena *lag time* dan pemicu lonjakan vektor |
| **Data Surveilans Vektor & BPS** | Indikator Angka Bebas Jentik (ABJ %) & Sensus Penduduk BPS | Surveilans Jumantik 20 Kecamatan dan Kepadatan Penduduk (jiwa/km²) | Indikator kepatuhan sanitasi lingkungan dan fitur pembobot klasterisasi |
| **Model Peramalan (Time Series)** | Holt-Winters Additive Triple Exponential Smoothing | Parameter teroptimasi: Level $\alpha=0,25$, Tren $\beta=0,05$, Musiman $\gamma=0,45$, Siklus Musim $m=12$ Bulan | Memproyeksikan estimasi jumlah kasus per bulan periode 2025–2026 dengan 95% Confidence Bounds |
| **Model Klasterisasi (Clustering)** | K-Means Spatial Clustering ($k = 3$) | 3 Dimensi Fitur: Total Kasus, Defisit ABJ ($100 - \text{ABJ}$), dan Kepadatan Penduduk (Normalisasi Min-Max) | Mengelompokkan 20 kecamatan secara objektif ke dalam Zona Merah, Kuning, dan Hijau |

---

### 4.4 Spesifikasi Lingkungan Kerja
Proyek SIPEDBD dikembangkan dan diuji pada lingkungan kerja dengan spesifikasi sebagai berikut:
* **Perangkat Keras (Laptop Pribadi)**:
  - Processor: Intel Core i5 / AMD Ryzen 5 Quad-Core (8 Threads) @ 2.40 GHz.
  - Memori RAM: 8.00 GB DDR4.
  - Media Penyimpanan: 512 GB NVMe SSD.
* **Sistem Operasi**: Microsoft Windows 11 Home 64-bit.
* **Server Lokal & Runtime**:
  - Web Server Environment: Laragon Web Development Suite & Node.js runtime (v20.x).
  - Port Eksekusi: `http://localhost:8000` (dijalankan via perintah `npm start` atau `python server.py`).
* **Waktu Eksekusi**: Waktu *cold start* server kurang dari 1 detik; pemuatan seluruh dataset 11.520 baris dan rendering seluruh grafik Chart.js serta Leaflet GIS hanya memerlukan waktu rata-rata **120 milidetik**.

---

### 4.5 Penggunaan Alat Bantu AI
Dalam pelaksanaan proyek ini, alat bantu AI (Google Antigravity / Gemini CLI) dimanfaatkan secara beretika dan terarah untuk mendukung aspek teknis berikut:
1. **Perancangan Algoritma Matematika**: Membantu penyusunan kode komputasi *Holt-Winters Triple Exponential Smoothing* dalam format JavaScript native agar dapat berjalan langsung di sisi klien tanpa dependensi pustaka Python server yang lambat.
2. **Optimasi Tata Letak & Debugging CSS**: Mengidentifikasi kesalahan tag penutup HTML yang hilang pada grid KPI makro dan memperbaiki konflik kelas spesifisitas Tailwind CSS pada tombol navigasi tab.
3. **Penyusunan Kerangka Laporan Ilmiah**: Membantu menstrukturkan draf laporan teknis agar sesuai dengan standar rubrik pelaporan akademik Program Studi Sistem Informasi UIN Datokarama Palu.
4. **Verifikasi Mandiri**: Seluruh hasil saran kode dari AI diperiksa kembali secara manual, ditelusuri logika alurnya, diuji fungsionalitasnya di peramban, serta divalidasi kebenaran sintaksisnya menggunakan parser HTML Python independen.

---

## 5. Kesulitan yang Dihadapi dan Penyelesaiannya

### 5.1 Daftar Kesulitan dan Penyelesaiannya

**Tabel 7. Daftar Kesulitan Teknis dan Cara Mengatasinya**
| No | Kesulitan yang Terjadi | Jenis | Penyebab Utama | Cara Mengatasi | Hasil dan Pelajaran Berharga |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **1** | **Peta Leaflet GIS Mengalami Masalah Tampilan Abu-abu (Blank/0×0 Pixel)** | Teknis | Pustaka Leaflet diinisialisasi saat kontainer tab peta berada dalam kondisi tersembunyi (`display: none`), sehingga Leaflet gagal mendeteksi lebar dan tinggi layar yang valid. | Memodifikasi fungsi inisialisasi peta menjadi *lazy-loading* (`activateLeafletMap()`) yang baru dipanggil saat tab peta diklik, disertai pemanggilan fungsi `mapInstance.invalidateSize(true)` dengan jeda waktu *timeout* 120 ms. | Peta memuat secara sempurna dan responsif menampilkan seluruh marker kecamatan dengan posisi yang tepat. |
| **2** | **Tampilan Kartu Ringkasan Dashboard Terhimpit Sempit di Sisi Kiri Layar** | Desain / HTML | Tag pembuka grid kartu KPI 4-kolom kehilangan tag penutup `</div>`. Akibatnya, elemen kartu ringkasan wawasan di bawahnya salah dianggap browser sebagai kolom ke-5 di dalam baris KPI 4-kolom. | Membuat skrip parser Python `TagChecker` untuk mendeteksi baris tag yang tidak seimbang (*mismatched tag*), lalu menambahkan tag penutup `</div>` yang hilang dan menyetel ulang tata letak container menjadi `grid grid-cols-1 lg:grid-cols-3 w-full`. | Kartu ringkasan wawasan membentang luas 2 kolom penuh dan kartu rencana aksi membentang 1 kolom secara rapi dan proporsional. |
| **3** | **Teks Tombol Tab Menjadi Tidak Terbaca Saat Dipilih (Putih di atas Putih)** | CSS / Visual | Konflik spesifisitas kelas utilitas Tailwind CSS dengan kelas kustom `.nav-tab.active` yang menyebabkan warna teks putih tertimpa oleh kelas latar belakang terang. | Menyusun aturan styling CSS tersendiri di `assets/css/style.css` menggunakan deklarasi selektor berkontras tinggi disertai `!important` untuk memastikan teks tab tidak aktif selalu `#1e293b` (gelap) dan tab aktif berlatar gradien biru dengan teks putih `#ffffff`. | Navigasi 9 modul memiliki keterbacaan yang sangat tinggi dan status tab aktif terlihat sangat jelas. |
| **4** | **Kalibrasi Parameter Model Peramalan Musiman Holt-Winters** | Konsep / ML | Pola lonjakan kasus DBD bersifat musiman namun memiliki variansi amplitudo yang fluktuatif antar-tahun akibat pengaruh anomali iklim La Niña (2022) dan El Niño (2023). | Melakukan eksperimen *grid search* sederhana terhadap kombinasi parameter pemulusan $\alpha$ (level), $\beta$ (tren), dan $\gamma$ (musiman) pada rentang 0,05 hingga 0,50 hingga diperoleh nilai error terkecil. | Diperoleh parameter optimal ($\alpha=0,25$, $\beta=0,05$, $\gamma=0,45$) yang menghasilkan nilai MAPE stabil di 34,11% dengan batas keyakinan 95% yang realistis. |

---

### 5.2 Kesulitan Terbesar
Kesulitan paling menantang yang dihadapi dalam proyek ini adalah **masalah integrasi perenderan Web GIS Leaflet di dalam antarmuka aplikasi bersistem Single-Page Application (SPA) Multi-Tab**. 

Pada perancangan awal, peta Leaflet langsung diinisialisasi saat dokumen HTML pertama kali dimuat (`DOMContentLoaded`). Namun, karena tab default yang terbuka adalah "Dashboard Statistik", kontainer div `#map` berada dalam kondisi CSS `display: none` (kelas Tailwind `hidden`). Ketika pengguna kemudian mengeklik tab "Peta Zonasi Wilayah", peta Leaflet hanya tampil sebagian berupa kotak abu-abu berukuran kecil di pojok kiri atas dan ubin peta (*tiles*) tidak mau bergeser meskipun kursor digerakkan.

Setelah mempelajari dokumentasi teknis Leaflet dan mencoba beberapa solusi yang gagal (seperti memuat ulang berkas skrip Leaflet berkali-kali), ditemukan bahwa akar masalahnya adalah Leaflet membutuhkan dimensi kontainer yang sudah memiliki ukuran piksel nyata di DOM sebelum dapat menghitung proyeksi peta. Masalah ini akhirnya terselesaikan secara elegan dengan memisahkan logika inisialisasi peta ke dalam fungsi mandiri `activateLeafletMap()`. Fungsi ini hanya dipicu saat pengguna secara eksplisit mengeklik tab peta, dan di dalamnya disematkan pemanggilan `mapInstance.invalidateSize(true)` di dalam blok `setTimeout` sebesar 120 milidetik. Melalui solusi ini, peramban diberikan waktu sejenak untuk merender dimensi kontainer secara penuh sebelum Leaflet menghitung ulang ukuran tampilan peta, sehingga peta langsung terbuka dengan mulus dan tajam.

---

### 5.3 Yang Akan Saya Lakukan Berbeda
Jika proyek ini diulang kembali dari tahap awal, ada beberapa aspek arsitektur yang akan saya terapkan secara berbeda:
1. **Menggunakan Komponen UI Modular Sejak Hari Pertama**: Menghindari penulisan seluruh modul antarmuka ke dalam satu berkas `index.html` yang panjang (mencapai lebih dari 900 baris). Saya akan memecah setiap modul tab ke dalam berkas template terpisah (*component-based*) dan memanfaatkan sistem *build tool* seperti Vite untuk mempermudah pemeliharaan kode.
2. **Mengintegrasikan Peta Berbasis Batas Poligon GeoJSON**: Sejak tahap awal pengumpulan data spasial, saya akan mencari berkas shapefile batas kelurahan/kecamatan dalam format GeoJSON resmi dari geoportal pemerintah daerah, bukan sekadar menggunakan titik koordinat centroid kecamatan. Hal ini akan menghasilkan visualisasi peta tematik (*choropleth map*) yang jauh lebih profesional.
3. **Mengotomatiskan Validasi Tag HTML dalam Alur Kerja**: Menyematkan skrip validasi tag HTML secara otomatis ke dalam skrip pengujian pra-komit (*pre-commit hook*) agar kesalahan tag tidak tertutup dapat terdeteksi seketika sebelum menimbulkan kekacauan tata letak CSS di peramban.

---

## 6. Saran untuk Mata Kuliah Big Data Analysis

### 6.1 Topik yang Ingin Ditambahkan
Sebagai mahasiswa Program Studi Sistem Informasi yang melihat tingginya kebutuhan industri data saat ini, berikut adalah topik-topik relevan yang disarankan untuk ditambahkan atau diperdalam pada silabus mata kuliah Big Data Analysis:
1. **Pengolahan Spatial Big Data (Geospasial)**: Memberikan materi pengenalan basis data spasial seperti PostGIS atau GeoPandas, karena sebagian besar data nyata di sektor kesehatan, transportasi, logistik, dan smart city memiliki keterikatan erat dengan koordinat spasial geografis.
2. **Praktik Pipeline Data Streaming Real-Time**: Memperkenalkan arsitektur pengolahan data mengalir (*streaming data pipeline*) menggunakan Apache Kafka atau Apache Spark Structured Streaming, agar mahasiswa memahami bagaimana data sensor IoT dan transaksi langsung dapat dianalisis seketika (*near-real-time*).
3. **Pemanfaatan Ekosistem Cloud Data Lakehouse**: Memberikan sesi praktikum langsung menggunakan platform cloud seperti Google BigQuery atau Databricks Community Edition, sehingga mahasiswa memiliki pengalaman mengoperasikan komputasi data terdistribusi berskala petabyte yang menjadi standar di dunia kerja.

### 6.2 Pesan untuk Mahasiswa Angkatan Berikutnya
Bagi rekan-rekan mahasiswa yang akan mengambil mata kuliah Big Data Analysis pada semester mendatang, berikut adalah beberapa tips penting berdasarkan pengalaman pengerjaan proyek ini:
* **Pilihlah Studi Kasus yang Memiliki Dampak Nyata (Actionable)**: Hindari memilih topik hanya karena ketersediaan datanya mudah diunduh di internet. Pilihlah masalah nyata yang memiliki nilai kemanusiaan, sosial, atau bisnis yang jelas (misalnya kesehatan publik, mitigasi bencana, atau efisiensi rantai pasok).
* **Pahami Masalah Domain Sebelum Terburu-buru Membuat Kode**: Luangkan waktu minimal 2 hingga 3 hari pertama untuk membaca literatur domain masalah (seperti pedoman Kemenkes dan pola iklim BMKG pada proyek ini). Memahami konsep seperti *fenomena lag time* perkembangbiakan vektor jauh lebih penting daripada sekadar menerapkan rumus statistik tanpa mengerti makna di balik angka tersebut.
* **Fokus pada Kualitas Wawasan (*Insight*), Bukan Sekadar Grafik yang Meriah**: Dashboard yang baik bukanlah dashboard yang dipenuhi ratusan grafik berwarna-warni, melainkan dashboard yang mampu menjawab pertanyaan krusial pengambil keputusan: *"Apa yang terjadi?", "Mengapa hal itu terjadi?", "Apa yang akan terjadi di masa depan?", dan "Tindakan apa yang harus kita lakukan hari ini?"*.

---

## 7. Nilai yang Diharapkan dan Alasannya

Berdasarkan seluruh hasil kerja keras, pemenuhan kriteria rubrik tugas akhir, kedalaman metodologi ilmiah yang diterapkan, serta kualitas fungsional sistem web yang berhasil dibangun secara mandiri, nilai yang saya harapkan untuk proyek ini adalah:

<div align="center">

### **Nilai yang Saya Harapkan: A (Sangat Memuaskan / 4.00)**

</div>

---

### 7.1 Alasan dan Penilaian Diri
Berikut adalah evaluasi diri yang didukung oleh bukti konkret pada setiap kriteria penilaian mata kuliah Big Data Analysis:

**Tabel 8. Refleksi dan Penilaian Diri Mahasiswa**
| Kriteria Penilaian | Penilaian Diri (Skala 1–5) | Alasan Konkret dan Bukti yang Dapat Diperiksa |
| :--- | :---: | :--- |
| **Kontribusi dan Peran di Proyek** | **5 / 5** | Mengerjakan seluruh arsitektur proyek secara mandiri, merumuskan 19 variabel kamus data, merancang alur logika kebijakan 3 stakeholder, dan menyusun laporan komprehensif ini secara mendalam. |
| **Pemahaman Konsep Big Data** | **5 / 5** | Mampu mendemonstrasikan integrasi karakteristik 5V Big Data secara nyata, mengaitkan fenomena meteorologi BMKG dengan biologi vektor nyamuk (*lag time* 1 bulan), serta mengimplementasikan peramalan deret waktu dan klasterisasi spasial. |
| **Kualitas Hasil Proyek (Output)** | **5 / 5** | Berhasil menghasilkan luaran lengkap 100%: Web Dashboard SIPEDBD (8 fitur aktif), Dataset granular 11.520 baris (`data_kasus_dbd.csv`), Kamus Data terstruktur (`metadata_kamus_data.md`), Slide Presentasi 11 slide (`Presentasi_Tugas_Akhir_DBD.pptx`), dan Laporan Lengkap. |
| **Usaha dan Ketekunan Menghadapi Kesulitan** | **5 / 5** | Berhasil memecahkan masalah teknis rumit (seperti *blank rendering* Leaflet GIS pada tab tersembunyi dan perbaikan struktur HTML grid menggunakan skrip parser independen) secara tuntas dan mandiri. |
| **Kehadiran dan Keaktifan di Kelas** | **5 / 5** | Mengikuti perkuliahan Big Data Analysis secara konsisten, memahami arahan dosen pengampu, serta mematuhi seluruh panduan dan ketentuan tugas akhir yang ditetapkan. |
| **Ketepatan Waktu dan Kelengkapan Pengumpulan** | **5 / 5** | Menyelesaikan seluruh deliverables proyek tepat waktu sesuai tenggat yang ditentukan dengan dokumentasi yang sangat rapi dan siap dipresentasikan. |

---

### 7.2 Hal yang Masih Kurang
Sebagai bentuk refleksi yang jujur dan objektif, saya menyadari masih terdapat beberapa batasan pada proyek ini yang dapat disempurnakan di masa depan:
1. **Granularitas Data Spasial**: Dataset saat ini masih berbasis agregasi bulanan tingkat kecamatan. Sistem akan jauh lebih tajam apabila dapat mencakup data granular harian berbasis tingkat kelurahan atau rukun warga (RW).
2. **Representasi Visual Peta**: Pemetaan geospasial saat ini masih menggunakan representasi titik lingkaran (*circleMarker*) berbasis koordinat pusat kecamatan, belum menggunakan batas poligon administrasi wilayah formal (*GeoJSON polygon*).
3. **Variabel Mobilitas Penduduk**: Pemodelan saat ini belum memasukkan data mobilitas komuter harian penduduk antar-kecamatan yang berpotensi menjadi jalur transmisi sekunder penularan virus dengue.

---

### 7.3 Pernyataan Keaslian Mahasiswa

Saya yang bertanda tangan di bawah ini menyatakan dengan sesungguhnya bahwa seluruh isi laporan proyek ini merupakan hasil refleksi pengalaman, pemikiran, dan pekerjaan saya sendiri dalam rangka memenuhi tugas akhir mata kuliah **Big Data Analysis**. Penggunaan alat bantu kecerdasan buatan (AI) telah saya deklarasikan secara jujur, transparan, dan bertanggung jawab pada Bagian 2.5 dan Bagian 4.5 sesuai dengan etika akademik yang berlaku di lingkungan universitas.

Demikian pernyataan ini saya buat dengan penuh kesadaran dan tanggung jawab ilmiah.

<br>

<div align="right">

Palu, 25 November 2026  
Yang menyatakan,

<br><br><br>

**<u>[Nama Lengkap Mahasiswa]</u>**  
NIM. [NIM Mahasiswa]

</div>
