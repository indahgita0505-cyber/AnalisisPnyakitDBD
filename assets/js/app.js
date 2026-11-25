/**
 * SIPEDBD - Sistem Informasi Prediksi dan Analisis DBD
 * Big Data Analytics Engine & Dashboard Controller
 */

document.addEventListener("DOMContentLoaded", function () {
    const data = window.DBD_DATA;
    if (!data) {
        console.error("Data DBD tidak ditemukan. Pastikan assets/js/data.js dimuat.");
        return;
    }

    // State Aplikasi
    let currentTab = "dashboard";
    let mapInstance = null;
    let mapMarkers = [];
    let currentMapTier = "all";
    let trendChart = null;
    let ageChart = null;
    let genderChart = null;
    let topKecChart = null;
    let forecastChart = null;
    let clusterScatterChart = null;

    // Inisialisasi Elemen
    initNavigation();
    initOverviewCards(data);
    initMultiDimCharts(data);
    initForecastSection(data);
    initClusteringSection(data);
    initRecommendations(data);
    initDataTable(data);
    initSimulators(data);

    // ==========================================
    // 1. NAVIGASI TABS (KONTRAST TINGGI & JELAS)
    // ==========================================
    function initNavigation() {
        const tabBtns = document.querySelectorAll(".nav-tab");
        const tabPanes = document.querySelectorAll(".tab-pane");
        const indicator = document.getElementById("active-tab-indicator");

        tabBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                const target = btn.getAttribute("data-tab");
                const title = btn.getAttribute("data-title") || btn.innerText.trim();

                // Bersihkan active state dari seluruh tombol
                tabBtns.forEach(b => b.classList.remove("active"));

                // Tambahkan active state ke tombol yang dipilih
                btn.classList.add("active");

                // Perbarui teks indikator navigasi aktif
                if (indicator) {
                    indicator.innerText = title;
                }

                // Tampilkan tab target, sembunyikan tab lainnya
                tabPanes.forEach(p => {
                    if (p.id === `tab-${target}`) {
                        p.classList.remove("hidden");
                    } else {
                        p.classList.add("hidden");
                    }
                });

                currentTab = target;

                // Handle khusus aktivasi PETA ZONASI WILAYAH
                if (target === "map") {
                    activateLeafletMap(data);
                } else if (target === "trends" && trendChart) {
                    setTimeout(() => {
                        trendChart.resize();
                        trendChart.update();
                    }, 100);
                } else if (target === "demography") {
                    setTimeout(() => {
                        if (ageChart) ageChart.resize();
                        if (genderChart) genderChart.resize();
                        if (topKecChart) topKecChart.resize();
                    }, 100);
                } else if (target === "forecast" && forecastChart) {
                    setTimeout(() => {
                        forecastChart.resize();
                        forecastChart.update();
                    }, 100);
                } else if (target === "clusters" && clusterScatterChart) {
                    setTimeout(() => {
                        clusterScatterChart.resize();
                        clusterScatterChart.update();
                    }, 100);
                }
            });
        });
    }

    // ==========================================
    // 2. DASHBOARD STATISTIK (OVERVIEW KPI)
    // ==========================================
    function initOverviewCards(data) {
        const sum = data.summary_global;
        document.getElementById("kpi-total-kasus").innerText = sum.total_kasus.toLocaleString("id-ID");
        document.getElementById("kpi-total-mati").innerText = sum.total_meninggal.toLocaleString("id-ID");
        document.getElementById("kpi-cfr").innerText = `${sum.cfr_persen}%`;
        document.getElementById("kpi-abj").innerText = `${sum.rata_rata_abj}%`;
        document.getElementById("kpi-merah").innerText = `${sum.kecamatan_zona_merah} Kec`;
        document.getElementById("kpi-kuning").innerText = `${sum.kecamatan_zona_kuning} Kec`;
        document.getElementById("kpi-hijau").innerText = `${sum.kecamatan_zona_hijau} Kec`;

        const statusBadge = document.getElementById("status-siaga-badge");
        if (sum.kecamatan_zona_merah > 4) {
            statusBadge.innerHTML = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-red-100 text-red-800 border border-red-200 shadow-xs">
                <span class="w-2.5 h-2.5 mr-1.5 bg-red-500 rounded-full animate-ping"></span>
                STATUS: SIAGA 1 (WASPADA MUSIM HUJAN)
            </span>`;
        }

        // Checklist Interaktif Rencana Aksi
        const checkboxes = document.querySelectorAll(".action-checkbox");
        const progressText = document.getElementById("checklist-progress-text");
        const progressBar = document.getElementById("checklist-progress-bar");

        function updateChecklist() {
            if (!checkboxes.length) return;
            let checkedCount = 0;
            checkboxes.forEach(cb => {
                const label = cb.closest("label");
                if (cb.checked) {
                    checkedCount++;
                    if (label) {
                        label.classList.add("bg-emerald-50/70", "border-emerald-200");
                        label.classList.remove("border-slate-100");
                    }
                } else {
                    if (label) {
                        label.classList.remove("bg-emerald-50/70", "border-emerald-200");
                        label.classList.add("border-slate-100");
                    }
                }
            });

            const pct = Math.round((checkedCount / checkboxes.length) * 100);
            if (progressBar) progressBar.style.width = `${pct}%`;
            if (progressText) {
                if (pct === 100) {
                    progressText.className = "text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-600 text-white shadow-xs";
                    progressText.innerText = "Semua Aksi Selesai (100%)";
                } else {
                    progressText.className = "text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800";
                    progressText.innerText = `${checkedCount}/${checkboxes.length} Selesai (${pct}%)`;
                }
            }
        }

        checkboxes.forEach(cb => {
            cb.addEventListener("change", updateChecklist);
        });
        updateChecklist();
    }

    // ==========================================
    // 3. ANALISIS TREN KASUS & DEMOGRAFI
    // ==========================================
    function initMultiDimCharts(data) {
        const monthly = data.monthly_series;
        const labels = monthly.map(m => m.periode);
        const cases = monthly.map(m => m.kasus);
        const rain = monthly.map(m => m.curah_hujan);

        const ctxTrend = document.getElementById("chart-trend-cases").getContext("2d");
        trendChart = new Chart(ctxTrend, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        type: "line",
                        label: "Jumlah Kasus DBD",
                        data: cases,
                        borderColor: "#0284c7",
                        backgroundColor: "rgba(2, 132, 199, 0.12)",
                        borderWidth: 2.5,
                        pointRadius: 2,
                        pointHoverRadius: 5,
                        yAxisID: "yCases",
                        tension: 0.3,
                        fill: true
                    },
                    {
                        type: "bar",
                        label: "Curah Hujan (mm)",
                        data: rain,
                        backgroundColor: "rgba(148, 163, 184, 0.45)",
                        hoverBackgroundColor: "rgba(148, 163, 184, 0.75)",
                        yAxisID: "yRain",
                        borderRadius: 3
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                interaction: { mode: "index", intersect: false },
                plugins: {
                    legend: { position: "top", labels: { font: { family: "Plus Jakarta Sans", weight: "bold" } } },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                if (context.dataset.yAxisID === "yCases") {
                                    return `Kasus DBD: ${context.parsed.y.toLocaleString("id-ID")} penderita`;
                                } else {
                                    return `Curah Hujan: ${context.parsed.y} mm`;
                                }
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: { maxTicksLimit: 14, font: { size: 10, weight: "600" } },
                        grid: { display: false }
                    },
                    yCases: {
                        type: "linear",
                        position: "left",
                        title: { display: true, text: "Jumlah Kasus", font: { weight: "bold" } },
                        grid: { color: "rgba(226, 232, 240, 0.6)" }
                    },
                    yRain: {
                        type: "linear",
                        position: "right",
                        title: { display: true, text: "Curah Hujan (mm)", font: { weight: "bold" } },
                        grid: { display: false }
                    }
                }
            }
        });

        // Demografi Usia
        const umur = data.demografi.kelompok_umur;
        const ctxAge = document.getElementById("chart-age-distribution").getContext("2d");
        ageChart = new Chart(ctxAge, {
            type: "doughnut",
            data: {
                labels: umur.map(u => u.label),
                datasets: [{
                    data: umur.map(u => u.kasus),
                    backgroundColor: ["#f59e0b", "#0284c7", "#3b82f6", "#ef4444"],
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "bottom", labels: { boxWidth: 12, font: { size: 11, weight: "600" } } },
                    tooltip: {
                        callbacks: {
                            label: function (ctx) {
                                const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                                const val = ctx.parsed;
                                const pct = ((val / total) * 100).toFixed(1);
                                return `${ctx.label}: ${val.toLocaleString("id-ID")} kasus (${pct}%)`;
                            }
                        }
                    }
                }
            }
        });

        // Distribusi Gender
        const gender = data.demografi.jenis_kelamin;
        const ctxGender = document.getElementById("chart-gender-distribution").getContext("2d");
        genderChart = new Chart(ctxGender, {
            type: "pie",
            data: {
                labels: gender.map(g => g.label),
                datasets: [{
                    data: gender.map(g => g.kasus),
                    backgroundColor: ["#0284c7", "#ec4899"],
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "bottom", labels: { boxWidth: 12, font: { size: 11, weight: "600" } } },
                    tooltip: {
                        callbacks: {
                            label: function (ctx) {
                                const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                                const val = ctx.parsed;
                                const pct = ((val / total) * 100).toFixed(1);
                                return `${ctx.label}: ${val.toLocaleString("id-ID")} kasus (${pct}%)`;
                            }
                        }
                    }
                }
            }
        });

        // Top 10 Kecamatan
        const sortedKec = [...data.kecamatan_clustered].sort((a, b) => b.total_kasus - a.total_kasus).slice(0, 10);
        const ctxTop = document.getElementById("chart-top-kecamatan").getContext("2d");
        topKecChart = new Chart(ctxTop, {
            type: "bar",
            data: {
                labels: sortedKec.map(k => k.nama),
                datasets: [{
                    label: "Total Kasus",
                    data: sortedKec.map(k => k.total_kasus),
                    backgroundColor: sortedKec.map(k => k.cluster_warna),
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: "y",
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => `Total Kasus: ${ctx.parsed.x.toLocaleString("id-ID")} kasus`
                        }
                    }
                },
                scales: {
                    x: { grid: { color: "rgba(226, 232, 240, 0.6)" } },
                    y: { grid: { display: false }, ticks: { font: { size: 11, weight: "600" } } }
                }
            }
        });

        const yearFilter = document.getElementById("filter-tahun-eda");
        if (yearFilter) {
            yearFilter.addEventListener("change", function () {
                const selectedYear = this.value;
                let filteredMonthly = data.monthly_series;
                if (selectedYear !== "all") {
                    filteredMonthly = filteredMonthly.filter(m => m.tahun === parseInt(selectedYear));
                }
                trendChart.data.labels = filteredMonthly.map(m => m.periode);
                trendChart.data.datasets[0].data = filteredMonthly.map(m => m.kasus);
                trendChart.data.datasets[1].data = filteredMonthly.map(m => m.curah_hujan);
                trendChart.update();
            });
        }
    }

    // ==========================================
    // 4. PEMETAAN ZONASI WILAYAH (LEAFLET GIS)
    // ==========================================
    function activateLeafletMap(data) {
        const mapContainer = document.getElementById("map");
        if (!mapContainer) return;

        const centerLat = -6.9147;
        const centerLng = 107.6098;

        // Inisialisasi peta hanya saat container terlihat dan belum ada instance
        if (!mapInstance) {
            mapInstance = L.map("map", {
                scrollWheelZoom: true
            }).setView([centerLat, centerLng], 12);

            L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
                maxZoom: 18,
                attribution: '© OpenStreetMap contributors'
            }).addTo(mapInstance);

            // Filter Map Buttons Listener
            const filterBtns = document.querySelectorAll(".map-filter-btn");
            filterBtns.forEach(btn => {
                btn.addEventListener("click", () => {
                    filterBtns.forEach(b => {
                        b.classList.remove("bg-sky-600", "text-white", "active-filter");
                        b.classList.add("bg-white", "text-slate-800");
                    });
                    btn.classList.remove("bg-white", "text-slate-800");
                    btn.classList.add("bg-sky-600", "text-white", "active-filter");

                    currentMapTier = btn.getAttribute("data-tier");
                    renderMapMarkers(data.kecamatan_clustered, currentMapTier);
                });
            });
        }

        // Render markers dan pastikan ukuran peta menyesuaikan layar
        setTimeout(() => {
            mapInstance.invalidateSize(true);
            mapInstance.setView([centerLat, centerLng], 12);
            renderMapMarkers(data.kecamatan_clustered, currentMapTier);
        }, 120);
    }

    function renderMapMarkers(kecamatanList, tierFilter) {
        if (!mapInstance) return;

        // Hapus marker sebelumnya
        mapMarkers.forEach(m => mapInstance.removeLayer(m));
        mapMarkers = [];

        kecamatanList.forEach(k => {
            if (tierFilter !== "all" && k.cluster_id.toString() !== tierFilter) {
                return;
            }

            const radius = Math.max(12, Math.min(26, k.total_kasus / 95));

            const circle = L.circleMarker([k.lat, k.lng], {
                radius: radius,
                fillColor: k.cluster_warna,
                color: "#ffffff",
                weight: 2.5,
                opacity: 1,
                fillOpacity: 0.85
            });

            const popupContent = `
                <div class="p-2.5 font-sans text-xs min-w-[230px]">
                    <div class="flex items-center justify-between gap-2 border-b pb-1.5 mb-2">
                        <strong class="text-sm font-bold text-slate-900">${k.nama}</strong>
                        <span class="px-2 py-0.5 rounded text-[10px] font-black text-white shadow-xs" style="background-color: ${k.cluster_warna}">${k.tingkat_risiko}</span>
                    </div>
                    <div class="grid grid-cols-2 gap-x-3 gap-y-1 text-slate-700 mb-2">
                        <div>Total Kasus: <strong class="text-slate-900">${k.total_kasus.toLocaleString("id-ID")}</strong></div>
                        <div>Kematian: <strong class="text-red-600">${k.total_meninggal}</strong> (${k.cfr_persen}%)</div>
                        <div>Angka Bebas Jentik: <strong class="text-slate-900">${k.avg_abj}%</strong></div>
                        <div>Kepadatan: <strong>${k.kepadatan.toLocaleString("id-ID")}</strong> /km²</div>
                    </div>
                    <div class="bg-slate-50 p-2 rounded border border-slate-200">
                        <span class="font-bold text-slate-900 block mb-0.5">Rekomendasi Intervensi:</span>
                        <p class="text-slate-600 leading-tight">${k.rekomendasi}</p>
                    </div>
                </div>
            `;

            circle.bindPopup(popupContent);
            circle.addTo(mapInstance);
            mapMarkers.push(circle);
        });
    }

    // ==========================================
    // 5. PREDIKSI KASUS DBD (TIME SERIES FORECASTING)
    // ==========================================
    function initForecastSection(data) {
        const fc = data.forecasting;
        const monthly = data.monthly_series;

        document.getElementById("eval-mae").innerText = `${fc.metrics.mae} Kasus`;
        document.getElementById("eval-rmse").innerText = `${fc.metrics.rmse} Kasus`;
        document.getElementById("eval-mape").innerText = `${fc.metrics.mape}%`;
        document.getElementById("eval-akurasi").innerText = `${fc.metrics.akurasi_model}%`;

        const histLabels = monthly.map(m => m.periode);
        const histCases = monthly.map(m => m.kasus);
        const histFitted = fc.fitted;

        const futureLabels = fc.future.map(f => f.periode);
        const futurePred = fc.future.map(f => f.prediksi);
        const futureLower = fc.future.map(f => f.lower_bound);
        const futureUpper = fc.future.map(f => f.upper_bound);

        const allLabels = [...histLabels, ...futureLabels];
        const allActual = [...histCases, ...new Array(futureLabels.length).fill(null)];
        const allFitted = [...histFitted, ...new Array(futureLabels.length).fill(null)];

        const allFuturePred = [...new Array(histLabels.length - 1).fill(null), histCases[histCases.length - 1], ...futurePred];
        const allFutureLower = [...new Array(histLabels.length - 1).fill(null), histCases[histCases.length - 1], ...futureLower];
        const allFutureUpper = [...new Array(histLabels.length - 1).fill(null), histCases[histCases.length - 1], ...futureUpper];

        const ctxFc = document.getElementById("chart-forecast-canvas").getContext("2d");
        forecastChart = new Chart(ctxFc, {
            type: "line",
            data: {
                labels: allLabels,
                datasets: [
                    {
                        label: "Kasus Aktual (2019-2024)",
                        data: allActual,
                        borderColor: "#0f172a",
                        backgroundColor: "#0f172a",
                        borderWidth: 2,
                        pointRadius: 2,
                        tension: 0.2
                    },
                    {
                        label: "Model In-Sample Fitted",
                        data: allFitted,
                        borderColor: "rgba(100, 116, 139, 0.6)",
                        borderDash: [4, 4],
                        borderWidth: 1.5,
                        pointRadius: 0,
                        tension: 0.2
                    },
                    {
                        label: "Prediksi Masa Depan (2025-2026)",
                        data: allFuturePred,
                        borderColor: "#ef4444",
                        backgroundColor: "#ef4444",
                        borderWidth: 2.5,
                        pointRadius: 3,
                        pointHoverRadius: 6,
                        tension: 0.2
                    },
                    {
                        label: "Batas Atas (95% CI)",
                        data: allFutureUpper,
                        borderColor: "rgba(239, 68, 68, 0.2)",
                        borderWidth: 1,
                        pointRadius: 0,
                        fill: "+1",
                        backgroundColor: "rgba(239, 68, 68, 0.15)",
                        tension: 0.2
                    },
                    {
                        label: "Batas Bawah (95% CI)",
                        data: allFutureLower,
                        borderColor: "rgba(239, 68, 68, 0.2)",
                        borderWidth: 1,
                        pointRadius: 0,
                        fill: false,
                        tension: 0.2
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                interaction: { mode: "index", intersect: false },
                plugins: {
                    legend: {
                        position: "top",
                        labels: {
                            font: { family: "Plus Jakarta Sans", weight: "bold" },
                            filter: function (item) {
                                return item.text !== "Batas Bawah (95% CI)";
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function (ctx) {
                                if (ctx.parsed.y !== null) {
                                    return `${ctx.dataset.label}: ${Math.round(ctx.parsed.y).toLocaleString("id-ID")} kasus`;
                                }
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: { maxTicksLimit: 18, font: { size: 10, weight: "600" } },
                        grid: { color: "rgba(241, 245, 249, 1)" }
                    },
                    y: {
                        title: { display: true, text: "Jumlah Kasus Prediksi / Bulan", font: { weight: "bold" } },
                        grid: { color: "rgba(226, 232, 240, 0.6)" }
                    }
                }
            }
        });
    }

    // ==========================================
    // 6. PENGELOMPOKAN WILAYAH (K-MEANS)
    // ==========================================
    function initClusteringSection(data) {
        const clusters = data.clusters_summary;
        const kec = data.kecamatan_clustered;

        const container = document.getElementById("cluster-summary-cards");
        container.innerHTML = "";

        clusters.forEach(c => {
            const card = document.createElement("div");
            card.className = "p-5 rounded-2xl border-2 bg-white shadow-sm flex flex-col justify-between";
            card.style.borderColor = c.warna;

            card.innerHTML = `
                <div>
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-black uppercase tracking-wider px-3 py-1 rounded-full text-white shadow-xs" style="background-color: ${c.warna}">
                            ${c.label}
                        </span>
                        <span class="text-sm font-extrabold text-slate-800">${c.jumlah_kecamatan} Kecamatan</span>
                    </div>
                    <div class="text-2xl font-black text-slate-900 mt-2">${c.total_kasus.toLocaleString("id-ID")} <span class="text-xs font-normal text-slate-500">Total Kasus</span></div>
                    <div class="text-xs text-slate-700 font-semibold mt-1 flex gap-4">
                        <span>Rata-rata ABJ: <strong class="text-slate-900">${c.rata_rata_abj}%</strong></span>
                        <span>CFR: <strong class="text-red-600">${c.cfr_persen}%</strong></span>
                    </div>
                    <div class="mt-3 pt-3 border-t text-xs text-slate-600">
                        <strong class="text-slate-900 block mb-1">Daftar Kecamatan:</strong>
                        <div class="flex flex-wrap gap-1">
                            ${c.daftar_kecamatan.map(k => `<span class="px-2 py-0.5 bg-slate-100 rounded text-[11px] font-semibold text-slate-700">${k}</span>`).join("")}
                        </div>
                    </div>
                </div>
                <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-700 bg-slate-50 p-2.5 rounded-lg">
                    <span class="font-bold text-slate-900 block mb-0.5">Strategi Intervensi:</span>
                    ${c.rekomendasi_utama}
                </div>
            `;
            container.appendChild(card);
        });

        // Scatter Plot 2D: Kasus vs ABJ
        const ctxScatter = document.getElementById("chart-cluster-scatter").getContext("2d");
        const scatterDatasets = [
            {
                label: "Zona Merah (Risiko Tinggi)",
                data: kec.filter(k => k.cluster_id === 1).map(k => ({ x: k.avg_abj, y: k.total_kasus, name: k.nama })),
                backgroundColor: "#ef4444",
                borderColor: "#b91c1c",
                pointRadius: 8
            },
            {
                label: "Zona Kuning (Risiko Sedang)",
                data: kec.filter(k => k.cluster_id === 2).map(k => ({ x: k.avg_abj, y: k.total_kasus, name: k.nama })),
                backgroundColor: "#eab308",
                borderColor: "#a16207",
                pointRadius: 8
            },
            {
                label: "Zona Hijau (Risiko Rendah)",
                data: kec.filter(k => k.cluster_id === 3).map(k => ({ x: k.avg_abj, y: k.total_kasus, name: k.nama })),
                backgroundColor: "#22c55e",
                borderColor: "#15803d",
                pointRadius: 8
            }
        ];

        clusterScatterChart = new Chart(ctxScatter, {
            type: "scatter",
            data: { datasets: scatterDatasets },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { font: { family: "Plus Jakarta Sans", weight: "bold" } } },
                    tooltip: {
                        callbacks: {
                            label: function (ctx) {
                                const pt = ctx.raw;
                                return `${pt.name}: ABJ ${pt.x}% | Kasus ${pt.y.toLocaleString("id-ID")}`;
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        title: { display: true, text: "Angka Bebas Jentik / ABJ (%)", font: { weight: "bold" } },
                        grid: { color: "rgba(226, 232, 240, 0.6)" }
                    },
                    y: {
                        title: { display: true, text: "Total Beban Kasus DBD", font: { weight: "bold" } },
                        grid: { color: "rgba(226, 232, 240, 0.6)" }
                    }
                }
            }
        });
    }

    // ==========================================
    // 7. SIMULATOR INTERAKTIF PENCEGAHAN
    // ==========================================
    function initSimulators(data) {
        const sliderABJ = document.getElementById("sim-slider-abj");
        const valABJ = document.getElementById("sim-val-abj");
        const resCases = document.getElementById("sim-res-cases");
        const resLives = document.getElementById("sim-res-lives");

        if (sliderABJ && valABJ) {
            sliderABJ.addEventListener("input", function () {
                const targetABJ = parseFloat(this.value);
                valABJ.innerText = `${targetABJ}%`;

                const deltaABJ = Math.max(0, targetABJ - 90.0);
                const reductionPct = Math.min(65, (deltaABJ * 4.8).toFixed(1));

                const baselineCases2025 = 6450;
                const savedCases = Math.round(baselineCases2025 * (reductionPct / 100));
                const savedLives = Math.round(savedCases * 0.0107);

                resCases.innerText = `-${savedCases.toLocaleString("id-ID")} Kasus (-${reductionPct}%)`;
                resLives.innerText = `~${savedLives} Nyawa Terselamatkan`;
            });
        }
    }

    // ==========================================
    // 8. REKOMENDASI & KALENDER
    // ==========================================
    function initRecommendations(data) {
        const calContainer = document.getElementById("kalender-intervensi-cards");
        if (calContainer) {
            calContainer.innerHTML = "";
            data.kalender_intervensi.forEach(k => {
                const item = document.createElement("div");
                item.className = "p-4 bg-white border border-slate-200 rounded-xl shadow-xs";
                item.innerHTML = `
                    <div class="flex items-center justify-between mb-1.5">
                        <span class="text-xs font-bold text-blue-600">${k.bulan}</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-800">${k.status}</span>
                    </div>
                    <p class="text-xs text-slate-700 font-medium">${k.aksi}</p>
                `;
                calContainer.appendChild(item);
            });
        }
    }

    // ==========================================
    // 9. MANAJEMEN DATASET (TABLE EXPLORER)
    // ==========================================
    function initDataTable(data) {
        const tbody = document.getElementById("raw-data-tbody");
        const searchInput = document.getElementById("data-search");
        const kecFilter = document.getElementById("data-filter-kec");

        let tableRecords = data.kecamatan_clustered;

        if (kecFilter) {
            data.kecamatan_clustered.forEach(k => {
                const opt = document.createElement("option");
                opt.value = k.nama;
                opt.innerText = k.nama;
                kecFilter.appendChild(opt);
            });
        }

        function renderTable(records) {
            tbody.innerHTML = "";
            if (records.length === 0) {
                tbody.innerHTML = `<tr><td colspan="7" class="text-center py-6 text-xs text-slate-500">Tidak ada data yang cocok dengan kriteria pencarian.</td></tr>`;
                return;
            }

            records.forEach(r => {
                const tr = document.createElement("tr");
                tr.className = "hover:bg-slate-50 transition text-xs border-b border-slate-100";
                tr.innerHTML = `
                    <td class="p-3 font-bold text-slate-900">${r.nama}</td>
                    <td class="p-3">
                        <span class="px-2.5 py-1 rounded-full text-[10px] font-black text-white shadow-xs" style="background-color: ${r.cluster_warna}">
                            ${r.tingkat_risiko}
                        </span>
                    </td>
                    <td class="p-3 text-slate-900 font-bold">${r.total_kasus.toLocaleString("id-ID")}</td>
                    <td class="p-3 text-red-600 font-bold">${r.total_meninggal}</td>
                    <td class="p-3 text-slate-800 font-semibold">${r.cfr_persen}%</td>
                    <td class="p-3 text-slate-900 font-bold">${r.avg_abj}%</td>
                    <td class="p-3 text-slate-700 max-w-xs truncate font-medium" title="${r.rekomendasi}">${r.rekomendasi}</td>
                `;
                tbody.appendChild(tr);
            });
        }

        renderTable(tableRecords);

        if (searchInput) {
            searchInput.addEventListener("input", function () {
                const query = this.value.toLowerCase();
                const filtered = tableRecords.filter(r => r.nama.toLowerCase().includes(query) || r.tingkat_risiko.toLowerCase().includes(query));
                renderTable(filtered);
            });
        }

        if (kecFilter) {
            kecFilter.addEventListener("change", function () {
                const val = this.value;
                if (val === "all") {
                    renderTable(tableRecords);
                } else {
                    renderTable(tableRecords.filter(r => r.nama === val));
                }
            });
        }

        const exportBtn = document.getElementById("btn-export-csv");
        if (exportBtn) {
            exportBtn.addEventListener("click", () => {
                window.location.href = "dataset/data_kasus_dbd.csv";
            });
        }
    }
});
