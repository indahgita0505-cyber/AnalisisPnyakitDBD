# SIPEDBD: Sistem Informasi Prediksi dan Analisis DBD

> **Tugas Akhir Mata Kuliah Big Data Analysis**  
> **Judul Project:** *"Analisis dan Prediksi Penyebaran Penyakit Demam Berdarah Dengue (DBD) Menggunakan Metode Time Series Forecasting dan Clustering Berbasis Web"*

[![Node.js](https://img.shields.io/badge/Node.js-v22-green.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![System](https://img.shields.io/badge/Platform-Web%20Dashboard%20(SPA)-sky.svg)]()

---

## 📖 Deskripsi Project

**SIPEDBD** (Sistem Informasi Prediksi dan Analisis DBD) adalah sistem berbasis web yang digunakan untuk menganalisis data historis kasus DBD, mengidentifikasi pola penyebaran berdasarkan waktu, wilayah, usia, dan jenis kelamin, serta memprediksi kemungkinan peningkatan kasus DBD pada periode mendatang.

Sistem ini dirancang untuk memfasilitasi pengambilan keputusan berbasis bukti (*evidence-based decision making*) bagi Dinas Kesehatan, Puskesmas, dan Komunitas Kader Jumantik melalui integrasi pemodelan deret waktu (*Time Series Forecasting*) dan segmentasi spasial (*K-Means Clustering*).

---

## 🌟 8 Fitur Utama Website SIPEDBD

Website SIPEDBD dilengkapi dengan 8 fitur utama yang saling terintegrasi:

1. **📊 Dashboard Statistik DBD**: Menyajikan ringkasan indikator makro (Total Kasus, Fatalitas CFR, Rata-rata ABJ Kota, Zonasi K-Means) serta status peringatan dini (*Early Warning System*).
2. **📈 Analisis Tren Kasus**: Visualisasi grafik deret waktu bulanan terpadu dengan data curah hujan BMKG, analisis fenomena *lag time* 1 bulan, dan siklus lonjakan tahunan.
3. **🗺️ Pemetaan Persebaran Wilayah**: Peta Web GIS berbasis Leaflet interaktif dengan marker pewarnaan klaster risiko dan popup detail tiap kecamatan.
4. **👥 Analisis Demografi Pasien**: Stratifikasi piramida kelompok usia (<5 thn, 5-14 thn, 15-44 thn, >44 thn), perbandingan gender L/P, serta analisis Case Fatality Rate (CFR).
5. **🔮 Prediksi Kasus DBD (Time Series Forecasting)**: Model Holt-Winters Additive Seasonality yang memproyeksikan kasus 24 bulan ke depan (2025–2026) lengkap dengan batas atas/bawah keyakinan 95% dan simulator interaktif.
6. **🎯 Pengelompokan Wilayah (K-Means Clustering)**: Segmentasi 20 kecamatan ke dalam 3 Klaster Risiko (Zona Merah, Kuning, Hijau) berbasis beban kasus, defisit ABJ, dan kepadatan penduduk.
7. **📋 Rekomendasi Tindakan Pencegahan**: Matriks kebijakan aksi bertingkat (Dinas Kesehatan, Puskesmas, Kader Jumantik) dan Kalender Musiman Intervensi 4 Kuartal.
8. **📑 Manajemen Dataset**: Eksplorasi tabel interaktif data granular (11.520 baris), pencarian instan, filter wilayah, dan tombol ekspor CSV.

---

## 🚀 Panduan Menjalankan Sistem SIPEDBD

### Cara 1: Menggunakan NPM (Paling Direkomendasikan)
Buka terminal pada direktori proyek, lalu jalankan:
```bash
npm start
```
*(atau `npm run dev`)*  
Server lokal akan aktif di `http://localhost:8000/` dan otomatis membuka browser Anda.

---

### Cara 2: Buka Langsung di Peramban Web (Tanpa Terminal)
Cukup **klik dua kali (double-click)** pada berkas:
```text
index.html
```
*Sistem langsung terbuka dan berfungsi 100% secara offline.*

---

### Cara 3: Menggunakan Python
Buka terminal pada direktori proyek, lalu jalankan:
```bash
python server.py
```
Akses di browser melalui: `http://localhost:8000`

---

### Cara 4: Melalui Laragon Web Server
Karena direktori proyek berada di `C:\laragon\www\AnalisisPnyakitDBD`, nyalakan Laragon lalu akses:
```text
http://localhost/AnalisisPnyakitDBD/
```
