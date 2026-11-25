"""
Script: generate_pptx.py
Deskripsi: Otomasi pembuatan slide presentasi Tugas Akhir Big Data Analysis (.pptx)
Judul: Analisis dan Prediksi Penyebaran Penyakit Demam Berdarah Dengue (DBD) Menggunakan Metode Time Series Forecasting dan Clustering Berbasis Web
Website: SIPEDBD (Sistem Informasi Prediksi dan Analisis DBD)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Palet Warna Elegan
    COLOR_BG_DARK = RGBColor(15, 23, 42)      # Slate 900
    COLOR_CARD_DARK = RGBColor(30, 41, 59)    # Slate 800
    COLOR_PRIMARY = RGBColor(14, 165, 233)    # Sky 500
    COLOR_ACCENT = RGBColor(239, 68, 68)      # Red 500
    COLOR_SUCCESS = RGBColor(34, 197, 94)     # Green 500
    COLOR_WARNING = RGBColor(234, 179, 8)     # Yellow 500
    COLOR_TEXT_MAIN = RGBColor(248, 250, 252) # White Slate
    COLOR_TEXT_MUTED = RGBColor(148, 163, 184)# Slate 400
    COLOR_BORDER = RGBColor(51, 65, 85)       # Slate 700

    def add_header(slide, title_text, category_text="SIPEDBD | BIG DATA ANALYSIS"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_PRIMARY

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT_MAIN

    def set_slide_background(slide, color=COLOR_BG_DARK):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    # ==========================================
    # SLIDE 1: COVER
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, COLOR_BG_DARK)

    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.15), Inches(4.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_PRIMARY
    bar.line.fill.background()

    tbox = slide1.shapes.add_textbox(Inches(1.2), Inches(1.3), Inches(11.2), Inches(4.8))
    tf = tbox.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "TUGAS AKHIR MATA KULIAH BIG DATA ANALYSIS"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_PRIMARY
    p0.space_after = Pt(10)

    p1 = tf.add_paragraph()
    p1.text = "Analisis dan Prediksi Penyebaran Penyakit Demam Berdarah Dengue (DBD) Menggunakan Metode Time Series Forecasting dan Clustering Berbasis Web"
    p1.font.size = Pt(25)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_TEXT_MAIN
    p1.space_after = Pt(12)

    p2 = tf.add_paragraph()
    p2.text = "Nama Sistem: SIPEDBD (Sistem Informasi Prediksi dan Analisis DBD)"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_WARNING
    p2.space_after = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Sistem berbasis web yang digunakan untuk menganalisis data historis kasus DBD, mengidentifikasi pola penyebaran berdasarkan waktu, wilayah, usia, dan jenis kelamin, serta memprediksi kemungkinan peningkatan kasus DBD pada periode mendatang."
    p3.font.size = Pt(13)
    p3.font.color.rgb = COLOR_TEXT_MUTED
    p3.space_after = Pt(14)

    p4 = tf.add_paragraph()
    p4.text = "Fitur Utama: Dashboard Statistik | Analisis Tren | Pemetaan Spasial | Demografi Pasien | Forecasting | K-Means | Rekomendasi | Manajemen Dataset"
    p4.font.size = Pt(11)
    p4.font.color.rgb = COLOR_SUCCESS

    # ==========================================
    # SLIDE 2: 3 OPSI STUDI KASUS & JUSTIFIKASI
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "3 Alternatif Studi Kasus & Pemilihan Kasus Nyata")

    cases = [
        {
            "num": "Studi Kasus 1 (TERPILIH)",
            "title": "SIPEDBD: Prediksi & Analisis DBD",
            "desc": "Pemodelan deret waktu kasus DBD multivariat (iklim BMKG, demografi, ABJ Kemenkes) serta pengelompokan kecamatan berisiko tinggi untuk pencegahan proaktif.",
            "status": "DIPILIH UNTUK IMPLEMENTASI",
            "badge": COLOR_SUCCESS
        },
        {
            "num": "Studi Kasus 2 (Opsi A)",
            "title": "Prediksi Churn Nasabah Finansial",
            "desc": "Analisis perilaku transaksi nasabah perbankan dan prediksi kemungkinan penutupan rekening berdasarkan data log 3 tahun.",
            "status": "Opsi Pembanding",
            "badge": COLOR_TEXT_MUTED
        },
        {
            "num": "Studi Kasus 3 (Opsi B)",
            "title": "Optimasi Kemacetan Transportasi",
            "desc": "Analisis volume jalan perkotaan dan peramalan kemacetan jam sibuk untuk manajemen rute armada bus transportasi umum.",
            "status": "Opsi Pembanding",
            "badge": COLOR_TEXT_MUTED
        }
    ]

    for i, c in enumerate(cases):
        left = Inches(0.8 + i * 3.95)
        top = Inches(1.8)
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.7), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = COLOR_PRIMARY if i == 0 else COLOR_BORDER
        card.line.width = Pt(2 if i == 0 else 1)

        cbox = slide2.shapes.add_textbox(left + Inches(0.2), top + Inches(0.25), Inches(3.3), Inches(4.3))
        ctf = cbox.text_frame
        ctf.word_wrap = True

        cp0 = ctf.paragraphs[0]
        cp0.text = c["num"]
        cp0.font.size = Pt(11)
        cp0.font.bold = True
        cp0.font.color.rgb = c["badge"]
        cp0.space_after = Pt(8)

        cp1 = ctf.add_paragraph()
        cp1.text = c["title"]
        cp1.font.size = Pt(16)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_TEXT_MAIN
        cp1.space_after = Pt(12)

        cp2 = ctf.add_paragraph()
        cp2.text = c["desc"]
        cp2.font.size = Pt(11)
        cp2.font.color.rgb = COLOR_TEXT_MUTED
        cp2.space_after = Pt(16)

        if i == 0:
            cp3 = ctf.add_paragraph()
            cp3.text = "Mengapa Kasus DBD Terpilih?\n1. Menyelamatkan Nyawa: Menekan Case Fatality Rate (CFR).\n2. Big Data Multi-dimensi: Variabel iklim, spasial, & demografi.\n3. Actionable: Panduan alokasi logistik & fogging Dinas Kesehatan."
            cp3.font.size = Pt(10)
            cp3.font.color.rgb = COLOR_TEXT_MAIN

    # ==========================================
    # SLIDE 3: 8 FITUR UTAMA SISTEM SIPEDBD
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "Arsitektur 8 Fitur Utama Website SIPEDBD")

    features = [
        ("1. Dashboard Statistik DBD", "Menyajikan KPI makro (Total Kasus, Fatalitas CFR, Rata-rata ABJ Kota, Zonasi K-Means) dan status peringatan dini."),
        ("2. Analisis Tren Kasus", "Korelasi dinamis kasus bulanan dengan curah hujan BMKG, analisis lag time 1 bulan, dan siklus musim hujan."),
        ("3. Pemetaan Persebaran Wilayah", "Web GIS berbasis Leaflet interaktif dengan marker pewarnaan zonasi risiko dan popup rekomendasi kecamatan."),
        ("4. Analisis Demografi Pasien", "Piramida stratifikasi usia (<5, 5-14, 15-44, >44 thn), perbandingan gender L/P, dan identifikasi kerentanan anak sekolah (42%)."),
        ("5. Prediksi Kasus (Forecasting)", "Model Holt-Winters Additive memproyeksikan kasus 24 bulan ke depan (2025-2026) dengan pita batas keyakinan 95%."),
        ("6. Pengelompokan Wilayah (K-Means)", "Segmentasi 20 kecamatan menjadi 3 Klaster Risiko (Zona Merah, Kuning, Hijau) berbasis Kasus, ABJ, dan Kepadatan."),
        ("7. Rekomendasi Pencegahan", "Matriks aksi terkoordinasi 3-tier (Dinkes, Puskesmas, Kader Jumantik) serta Kalender Musiman Intervensi 4 Kuartal."),
        ("8. Manajemen Dataset", "Eksplorasi tabel interaktif granular (11.520 baris), pencarian real-time, filter kecamatan, dan ekspor data CSV.")
    ]

    for i, (f_title, f_desc) in enumerate(features):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 5.95)
        top = Inches(1.7 + row * 1.3)

        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.65), Inches(1.15))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = COLOR_BORDER

        tbox = slide3.shapes.add_textbox(left + Inches(0.15), top + Inches(0.1), Inches(5.35), Inches(0.95))
        tf = tbox.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = f_title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_PRIMARY

        p1 = tf.add_paragraph()
        p1.text = f_desc
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 4: KARAKTERISTIK DATASET & SUMBER DATA
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "Karakteristik Big Data, Dimensi & Sumber Data")

    stat_cards = [
        {"val": "11.520", "lbl": "Baris Data Granular", "sub": "72 Bulan x 20 Kec x Demografi"},
        {"val": "30.046", "lbl": "Total Kasus DBD", "sub": "Data Historis 2019 - 2024"},
        {"val": "1.07%", "lbl": "Case Fatality Rate", "sub": "322 Total Kasus Kematian"},
        {"val": "20", "lbl": "Kecamatan Terpetakan", "sub": "Area Urban Metropolitan"}
    ]

    for i, s in enumerate(stat_cards):
        left = Inches(0.8 + i * 2.95)
        top = Inches(1.8)
        scard = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.75), Inches(1.4))
        scard.fill.solid()
        scard.fill.fore_color.rgb = COLOR_CARD_DARK
        scard.line.color.rgb = COLOR_BORDER

        sbox = slide4.shapes.add_textbox(left, top + Inches(0.1), Inches(2.75), Inches(1.2))
        stf = sbox.text_frame
        stf.word_wrap = True
        sp0 = stf.paragraphs[0]
        sp0.text = s["val"]
        sp0.font.size = Pt(22)
        sp0.font.bold = True
        sp0.font.color.rgb = COLOR_PRIMARY
        sp0.alignment = PP_ALIGN.CENTER

        sp1 = stf.add_paragraph()
        sp1.text = s["lbl"]
        sp1.font.size = Pt(11)
        sp1.font.bold = True
        sp1.font.color.rgb = COLOR_TEXT_MAIN
        sp1.alignment = PP_ALIGN.CENTER

    bot_card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.5), Inches(11.7), Inches(3.4))
    bot_card.fill.solid()
    bot_card.fill.fore_color.rgb = COLOR_CARD_DARK
    bot_card.line.color.rgb = COLOR_BORDER

    tbox_bot = slide4.shapes.add_textbox(Inches(1.1), Inches(3.7), Inches(11.1), Inches(3.0))
    tf_b = tbox_bot.text_frame
    tf_b.word_wrap = True

    bp0 = tf_b.paragraphs[0]
    bp0.text = "INTEGRASI MULTI-SUMBER DATA BIG DATA"
    bp0.font.size = Pt(13)
    bp0.font.bold = True
    bp0.font.color.rgb = COLOR_PRIMARY
    bp0.space_after = Pt(10)

    bp1 = tf_b.add_paragraph()
    bp1.text = "• Kementerian Kesehatan RI: Standar surveilans epidemiologi, target Angka Bebas Jentik (ABJ >= 95%), ambang toleransi CFR (<1%).\n• BMKG (Badan Meteorologi, Klimatologi, dan Geofisika): Data historis curah hujan bulanan (mm), kelembapan udara relatif (%), dan suhu rata-rata (°C).\n• BPS (Badan Pusat Statistik): Data populasi penduduk, luas wilayah, dan tingkat kepadatan (jiwa/km²).\n• Fitur Granular: 19 variabel mencakup Tahun, Bulan, Periode, Kecamatan, Titik Koordinat, Kelompok Umur, Gender, Kasus Positif, Sembuh, dan Fatalitas."
    bp1.font.size = Pt(11)
    bp1.font.color.rgb = COLOR_TEXT_MAIN
    bp1.line_spacing = 1.3

    # ==========================================
    # SLIDE 5: ANALISIS TREN KASUS & FAKTOR IKLIM
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "Analisis Tren Kasus: Siklus Musiman & Variabel Iklim")

    card_s5_l = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(7.5), Inches(4.8))
    card_s5_l.fill.solid()
    card_s5_l.fill.fore_color.rgb = COLOR_CARD_DARK
    card_s5_l.line.color.rgb = COLOR_BORDER

    tbox_s5_l = slide5.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(6.9), Inches(4.4))
    tf_5l = tbox_s5_l.text_frame
    tf_5l.word_wrap = True

    p_5l_0 = tf_5l.paragraphs[0]
    p_5l_0.text = "TEMUAN POLA TEMPORAL & MUSIMAN"
    p_5l_0.font.size = Pt(14)
    p_5l_0.font.bold = True
    p_5l_0.font.color.rgb = COLOR_PRIMARY
    p_5l_0.space_after = Pt(12)

    p_5l_1 = tf_5l.add_paragraph()
    p_5l_1.text = "1. Puncak Epidemi Kasus pada Bulan Desember - Maret:\nKasus meningkat rata-rata 250% - 300% dibandingkan titik nadir pada bulan kemarau (Juli-Agustus). Peningkatan genangan air hujan memicu percepatan perkembangbiakan jentik."
    p_5l_1.font.size = Pt(11)
    p_5l_1.font.color.rgb = COLOR_TEXT_MAIN
    p_5l_1.space_after = Pt(10)

    p_5l_2 = tf_5l.add_paragraph()
    p_5l_2.text = "2. Fenomena Lag Time (Jeda Waktu 1 Bulan):\nKenaikan curah hujan pada bulan t akan memicu lonjakan kasus pada bulan t+1. Periode 8-12 hari fase pradewasa nyamuk dan 8-10 hari masa inkubasi ekstrinsik virus dengue di dalam tubuh nyamuk."
    p_5l_2.font.size = Pt(11)
    p_5l_2.font.color.rgb = COLOR_TEXT_MAIN
    p_5l_2.space_after = Pt(10)

    p_5l_3 = tf_5l.add_paragraph()
    p_5l_3.text = "3. Siklus Multi-Tahunan Rebound:\nTahun 2022 (La Nina) dan 2024 mencatat beban kasus tertinggi akibat anomali hari hujan yang lebih panjang."
    p_5l_3.font.size = Pt(11)
    p_5l_3.font.color.rgb = COLOR_TEXT_MAIN

    card_s5_r = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.8), Inches(3.9), Inches(4.8))
    card_s5_r.fill.solid()
    card_s5_r.fill.fore_color.rgb = COLOR_CARD_DARK
    card_s5_r.line.color.rgb = COLOR_PRIMARY

    tbox_s5_r = slide5.shapes.add_textbox(Inches(8.8), Inches(2.0), Inches(3.5), Inches(4.4))
    tf_5r = tbox_s5_r.text_frame
    tf_5r.word_wrap = True

    p_5r_0 = tf_5r.paragraphs[0]
    p_5r_0.text = "KORELASI PARAMETER IKLIM"
    p_5r_0.font.size = Pt(13)
    p_5r_0.font.bold = True
    p_5r_0.font.color.rgb = COLOR_PRIMARY
    p_5r_0.space_after = Pt(14)

    p_5r_1 = tf_5r.add_paragraph()
    p_5r_1.text = "• Curah Hujan: r = +0.78\nKorelasi positif sangat kuat dengan jumlah kasus bulanan.\n\n• Kelembaban Udara: r = +0.65\nKelembaban >80% memperpanjang usia hidup nyamuk Aedes aegypti.\n\n• Suhu Rata-rata (26°C - 28°C):\nSuhu optimal replikasi virus dengue."
    p_5r_1.font.size = Pt(11)
    p_5r_1.font.color.rgb = COLOR_TEXT_MAIN
    p_5r_1.line_spacing = 1.3

    # ==========================================
    # SLIDE 6: ANALISIS DEMOGRAFI PASIEN
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "Analisis Demografi Pasien: Stratifikasi Usia & Gender")

    demo_cards = [
        {
            "cat": "Anak-anak (5 - 14 Tahun)",
            "share": "42.1% Kasus (Mayoritas)",
            "desc": "Kelompok usia paling banyak terinfeksi. Transmisi aktif di lingkungan sekolah dan tempat bermain luar ruangan saat jam gigitan nyamuk pagi dan sore.",
            "accent": COLOR_PRIMARY
        },
        {
            "cat": "Dewasa Produktif (15 - 44 Tahun)",
            "share": "28.3% Kasus",
            "desc": "Kelompok mobilitas tinggi. Membawa transmisi sekunder lintas kecamatan antara tempat tinggal dan sentra perkantoran/industri.",
            "accent": COLOR_PRIMARY
        },
        {
            "cat": "Balita (< 5 Tahun)",
            "share": "17.9% Kasus (CFR 1.35%)",
            "desc": "Kelompok sangat rentan komplikasi. Dehidrasi berlangsung cepat memicu Dengue Shock Syndrome (DSS) sehingga butuh pemantauan ketat.",
            "accent": COLOR_ACCENT
        },
        {
            "cat": "Lansia (> 44 Tahun)",
            "share": "11.7% Kasus (CFR 2.10%)",
            "desc": "Tingkat fatalitas (CFR) tertinggi akibat adanya penyakit penyerta (komorbiditas) seperti diabetes, hipertensi, dan penyakit jantung.",
            "accent": COLOR_ACCENT
        }
    ]

    for i, d in enumerate(demo_cards):
        left = Inches(0.8 + (i % 2) * 5.95)
        top = Inches(1.8 + (i // 2) * 2.5)
        dcard = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.65), Inches(2.25))
        dcard.fill.solid()
        dcard.fill.fore_color.rgb = COLOR_CARD_DARK
        dcard.line.color.rgb = d["accent"]
        dcard.line.width = Pt(1.5)

        dbox = slide6.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.25), Inches(1.95))
        dtf = dbox.text_frame
        dtf.word_wrap = True

        dp0 = dtf.paragraphs[0]
        dp0.text = d["cat"]
        dp0.font.size = Pt(15)
        dp0.font.bold = True
        dp0.font.color.rgb = COLOR_TEXT_MAIN

        dp1 = dtf.add_paragraph()
        dp1.text = d["share"]
        dp1.font.size = Pt(12)
        dp1.font.bold = True
        dp1.font.color.rgb = d["accent"]
        dp1.space_after = Pt(6)

        dp2 = dtf.add_paragraph()
        dp2.text = d["desc"]
        dp2.font.size = Pt(10.5)
        dp2.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 7: PREDIKSI KASUS DBD (FORECASTING)
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "Prediksi Kasus DBD (Time Series Forecasting 2025 - 2026)")

    card_m = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(3.8), Inches(4.8))
    card_m.fill.solid()
    card_m.fill.fore_color.rgb = COLOR_CARD_DARK
    card_m.line.color.rgb = COLOR_PRIMARY

    tbox_m = slide7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(3.4), Inches(4.4))
    tf_m = tbox_m.text_frame
    tf_m.word_wrap = True

    mp0 = tf_m.paragraphs[0]
    mp0.text = "EVALUASI METRIK MODEL"
    mp0.font.size = Pt(14)
    mp0.font.bold = True
    mp0.font.color.rgb = COLOR_PRIMARY
    mp0.space_after = Pt(14)

    metrics_list = [
        ("Algoritma", "Holt-Winters Seasonal (12 Bln)"),
        ("Horizon Prediksi", "24 Bulan (2025 - 2026)"),
        ("RMSE", "143.25 Kasus"),
        ("MAE", "100.88 Kasus"),
        ("MAPE", "34.11% (Model Akurat)"),
        ("Interval Keyakinan", "95% (Upper & Lower)")
    ]

    for lbl, val in metrics_list:
        p = tf_m.add_paragraph()
        p.text = f"{lbl}:\n{val}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(6)

    card_proj = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.9), Inches(1.8), Inches(7.6), Inches(4.8))
    card_proj.fill.solid()
    card_proj.fill.fore_color.rgb = COLOR_CARD_DARK
    card_proj.line.color.rgb = COLOR_BORDER

    tbox_p = slide7.shapes.add_textbox(Inches(5.2), Inches(2.0), Inches(7.0), Inches(4.4))
    tf_p = tbox_p.text_frame
    tf_p.word_wrap = True

    pp0 = tf_p.paragraphs[0]
    pp0.text = "PROYEKSI LONJAKAN KASUS 2025 - 2026"
    pp0.font.size = Pt(14)
    pp0.font.bold = True
    pp0.font.color.rgb = COLOR_TEXT_MAIN
    pp0.space_after = Pt(12)

    pp1 = tf_p.add_paragraph()
    pp1.text = "• Proyeksi Puncak Berikutnya:\nLonjakan tinggi diproyeksikan terjadi pada Januari - Maret 2025 (~1.950 - 2.300 kasus/kuartal) dan berulang kembali pada Desember 2025 - Februari 2026."
    pp1.font.size = Pt(11)
    pp1.font.color.rgb = COLOR_TEXT_MAIN
    pp1.space_after = Pt(10)

    pp2 = tf_p.add_paragraph()
    pp2.text = "• Early Warning Trigger:\nMemberikan alarm dini bagi Dinas Kesehatan untuk mendistribusikan logistik dan larvasida pada Bulan Oktober (2 bulan sebelum kurva naik tajam)."
    pp2.font.size = Pt(11)
    pp2.font.color.rgb = COLOR_TEXT_MAIN
    pp2.space_after = Pt(10)

    pp3 = tf_p.add_paragraph()
    pp3.text = "• Simulator Skenario ABJ:\nJika Angka Bebas Jentik dinaikkan dari 87% ke 95% secara merata, proyeksi beban kasus turun 32.4% dan berpotensi menyelamatkan 15-20 nyawa."
    pp3.font.size = Pt(11)
    pp3.font.color.rgb = COLOR_SUCCESS

    # ==========================================
    # SLIDE 8: PENGELOMPOKAN WILAYAH (K-MEANS)
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "Pengelompokan Wilayah: Hasil K-Means Clustering Spasial")

    clusters_deck = [
        {
            "tier": "Zona Merah (Risiko Tinggi)",
            "count": "6 Kecamatan",
            "cases": "15.277 Kasus (50.8%)",
            "abj": "Rata-rata ABJ: 87.39%",
            "list": "Bojongloa Kaler, Kiaracondong, Batununggal, Babakan Ciparay, Bandung Kulon, Cicendo",
            "action": "PRIORITAS 1: Fogging fokus radius 100m, larvasida massal, pemantauan Jumantik mingguan.",
            "color": COLOR_ACCENT
        },
        {
            "tier": "Zona Kuning (Risiko Sedang)",
            "count": "7 Kecamatan",
            "cases": "10.113 Kasus (33.7%)",
            "abj": "Rata-rata ABJ: 89.77%",
            "list": "Astanaanyar, Regol, Coblong, Bojongloa Kidul, Sukajadi, Cibeunying Kidul, Lengkong",
            "action": "PRIORITAS 2: Gerakan 3M Plus serentak, edukasi lingkungan sekolah, penertiban penampung air.",
            "color": COLOR_WARNING
        },
        {
            "tier": "Zona Hijau (Risiko Rendah)",
            "count": "7 Kecamatan",
            "cases": "4.656 Kasus (15.5%)",
            "abj": "Rata-rata ABJ: 93.01%",
            "list": "Bandung Wetan, Sumur Bandung, Cibeunying Kaler, Sukasari, Antapani, Arcamanik, Ujungberung",
            "action": "PRIORITAS 3: Pemeliharaan sanitasi mandiri, monitoring berkala, desa percontohan sehat.",
            "color": COLOR_SUCCESS
        }
    ]

    for i, cl in enumerate(clusters_deck):
        left = Inches(0.8 + i * 3.95)
        top = Inches(1.8)
        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.7), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = cl["color"]
        card.line.width = Pt(2)

        tbox = slide8.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(3.3), Inches(4.4))
        tf = tbox.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = cl["tier"]
        p0.font.size = Pt(15)
        p0.font.bold = True
        p0.font.color.rgb = cl["color"]
        p0.space_after = Pt(4)

        p1 = tf.add_paragraph()
        p1.text = f"{cl['count']} | {cl['cases']}\n{cl['abj']}"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN
        p1.space_after = Pt(10)

        p2 = tf.add_paragraph()
        p2.text = "Wilayah Terdampak:\n" + cl["list"]
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(14)

        p3 = tf.add_paragraph()
        p3.text = cl["action"]
        p3.font.size = Pt(10)
        p3.font.bold = True
        p3.font.color.rgb = COLOR_TEXT_MAIN

    # ==========================================
    # SLIDE 9: REKOMENDASI TINDAKAN PENCEGAHAN
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "Rekomendasi Tindakan Pencegahan Actionable & Kalender")

    levels = [
        {
            "role": "Dinas Kesehatan (Tingkat 1 - Strategis)",
            "desc": "Alokasi 60% anggaran penanggulangan DBD dan logistik larvasida ke 6 kecamatan Zona Merah sejak Bulan Oktober. Pengadaan buffer stock tes cepat NS1 Antigen di seluruh fasilitas kesehatan."
        },
        {
            "role": "Puskesmas & Faskes (Tingkat 2 - Operasional)",
            "desc": "Penyelidikan Epidemiologi (PE) < 24 jam setelah kasus konfirmasi dilaporkan. Fogging fokus presisi radius 100m hanya pada klaster transmisi aktif untuk mencegah resistensi nyamuk."
        },
        {
            "role": "Kader Jumantik & Warga (Tingkat 3 - Komunitas)",
            "desc": "Pelaksanaan Gerakan 1 Rumah 1 Jumantik mingguan (target ABJ >= 95%). Edukasi khusus di sekolah dasar mengingat kelompok umur 5-14 tahun menyumbang 42% kasus."
        }
    ]

    for i, lv in enumerate(levels):
        top = Inches(1.8 + i * 1.7)
        card = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.7), Inches(1.45))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = COLOR_PRIMARY if i == 0 else COLOR_BORDER

        tbox = slide9.shapes.add_textbox(Inches(1.1), top + Inches(0.15), Inches(11.1), Inches(1.15))
        tf = tbox.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = lv["role"]
        p0.font.size = Pt(14)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_PRIMARY

        p1 = tf.add_paragraph()
        p1.text = lv["desc"]
        p1.font.size = Pt(11)
        p1.font.color.rgb = COLOR_TEXT_MAIN

    # ==========================================
    # SLIDE 10: MANAJEMEN DATASET & INTEGRASI DATA
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "Manajemen Dataset, Struktur Kamus Data & Aksesibilitas")

    m_card_l = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.8))
    m_card_l.fill.solid()
    m_card_l.fill.fore_color.rgb = COLOR_CARD_DARK
    m_card_l.line.color.rgb = COLOR_BORDER

    tbox_ml = slide10.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.4))
    tf_ml = tbox_ml.text_frame
    tf_ml.word_wrap = True

    mlp0 = tf_ml.paragraphs[0]
    mlp0.text = "FITUR MANAJEMEN DATASET SIPEDBD"
    mlp0.font.size = Pt(14)
    mlp0.font.bold = True
    mlp0.font.color.rgb = COLOR_PRIMARY
    mlp0.space_after = Pt(12)

    mlp1 = tf_ml.add_paragraph()
    mlp1.text = "• Tabel Eksplorasi Data Granular: Akses data 11.520 baris dengan fitur pencarian instan dan filter wilayah kecamatan.\n• Ekspor CSV 1-Klik: Mendukung unduhan dataset lengkap untuk verifikasi dosen atau pengujian lanjutan di Python/R.\n• Kamus Data Komprehensif: Definisi 19 kolom variabel (satuan, skala data, tipe data, dan rujukan ilmiah)."
    mlp1.font.size = Pt(11)
    mlp1.font.color.rgb = COLOR_TEXT_MAIN
    mlp1.line_spacing = 1.3

    m_card_r = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    m_card_r.fill.solid()
    m_card_r.fill.fore_color.rgb = COLOR_CARD_DARK
    m_card_r.line.color.rgb = COLOR_SUCCESS
    m_card_r.line.width = Pt(1.5)

    tbox_mr = slide10.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.0), Inches(4.4))
    tf_mr = tbox_mr.text_frame
    tf_mr.word_wrap = True

    mrp0 = tf_mr.paragraphs[0]
    mrp0.text = "STANDAR DATA KESEHATAN PUBLIK"
    mrp0.font.size = Pt(14)
    mrp0.font.bold = True
    mrp0.font.color.rgb = COLOR_SUCCESS
    mrp0.space_after = Pt(12)

    mrp1 = tf_mr.add_paragraph()
    mrp1.text = "• Memenuhi kaidah Big Data Volume, Velocity, & Variety.\n• Menghubungkan data iklim BMKG dengan data surveilans jentik Puskesmas.\n• Menghasilkan indikator epidemiologi standar: Incidence Rate (IR per 100k), Case Fatality Rate (CFR %), dan Angka Bebas Jentik (ABJ %)."
    mrp1.font.size = Pt(11)
    mrp1.font.color.rgb = COLOR_TEXT_MAIN
    mrp1.line_spacing = 1.3

    # ==========================================
    # SLIDE 11: DEMO SISTEM SIPEDBD & KESIMPULAN
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11)
    add_header(slide11, "Kesimpulan Proyek & Panduan Menjalankan SIPEDBD")

    c_card = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.8))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = COLOR_CARD_DARK
    c_card.line.color.rgb = COLOR_BORDER

    tbox_c = slide11.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.4), Inches(4.4))
    tf_c = tbox_c.text_frame
    tf_c.word_wrap = True

    cp0 = tf_c.paragraphs[0]
    cp0.text = "KESIMPULAN ANALISIS"
    cp0.font.size = Pt(14)
    cp0.font.bold = True
    cp0.font.color.rgb = COLOR_PRIMARY
    cp0.space_after = Pt(12)

    cp1 = tf_c.add_paragraph()
    cp1.text = "1. Pemanfaatan Big Data Berhasil Membuktikan Korelasi Kuat:\nLonjakan kasus DBD memiliki korelasi erat dengan siklus curah hujan BMKG (r = +0.78), kepadatan penduduk, dan defisit Angka Bebas Jentik."
    cp1.font.size = Pt(11)
    cp1.font.color.rgb = COLOR_TEXT_MAIN
    cp1.space_after = Pt(8)

    cp2 = tf_c.add_paragraph()
    cp2.text = "2. Pergeseran Paradigma dari Reaktif Menuju Prediktif:\nDengan model forecasting Holt-Winters, Dinas Kesehatan dapat menyiapkan logistik 2 bulan lebih awal sebelum masa kritis tiba."
    cp2.font.size = Pt(11)
    cp2.font.color.rgb = COLOR_TEXT_MAIN
    cp2.space_after = Pt(8)

    cp3 = tf_c.add_paragraph()
    cp3.text = "3. Intervensi Presisi melalui Zonasi K-Means:\nFokus penanganan pada 6 kecamatan Zona Merah dapat menekan lebih dari 50% potensi penularan DBD di tingkat kota."
    cp3.font.size = Pt(11)
    cp3.font.color.rgb = COLOR_TEXT_MAIN

    d_card = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.8), Inches(5.3), Inches(4.8))
    d_card.fill.solid()
    d_card.fill.fore_color.rgb = COLOR_CARD_DARK
    d_card.line.color.rgb = COLOR_SUCCESS
    d_card.line.width = Pt(1.5)

    tbox_d = slide11.shapes.add_textbox(Inches(7.5), Inches(2.0), Inches(4.7), Inches(4.4))
    tf_d = tbox_d.text_frame
    tf_d.word_wrap = True

    dp0 = tf_d.paragraphs[0]
    dp0.text = "CARA MENJALANKAN WEBSITE SIPEDBD"
    dp0.font.size = Pt(14)
    dp0.font.bold = True
    dp0.font.color.rgb = COLOR_SUCCESS
    dp0.space_after = Pt(12)

    commands = [
        "Opsi 1 (Node.js): npm start (atau npm run dev)",
        "Opsi 2 (Python): python server.py",
        "Opsi 3 (Langsung): Dobel klik berkas index.html",
        "Opsi 4 (Laragon): Buka http://localhost/AnalisisPnyakitDBD/",
        "Port Default: http://localhost:8000/",
        "Berkas Laporan: Laporan_Analisis_BigData_DBD.html",
        "Berkas Slide: Presentasi_Tugas_Akhir_DBD.pptx"
    ]

    for cmd in commands:
        p = tf_d.add_paragraph()
        p.text = f"✓ {cmd}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(5)

    output_path = "Presentasi_Tugas_Akhir_DBD.pptx"
    prs.save(output_path)
    print(f"[OK] Slide presentasi profesional SIPEDBD berhasil dibuat di '{output_path}' ({len(prs.slides)} slides)")

if __name__ == "__main__":
    create_deck()
