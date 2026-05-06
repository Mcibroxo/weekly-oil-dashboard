# 🛢️ Weekly Petroleum Status Report (WPSR) Dashboard

An interactive, high-fidelity, and fully filtered analytics dashboard summarizing the weekly physical flows and stockpiles in the U.S. oil and petroleum markets. 

This project processes the dense, multi-structured spreadsheet published weekly by the **U.S. Energy Information Administration (EIA)**, filters out non-oil rows (like biofuels, NGLs, oxygenates), separates inventory levels from flow rates, and visualizes them inside a premium single-page web dashboard.

---

## ✨ Features
* **🎯 Focused Dataset:** Strips out hundreds of irrelevant rows to highlight core crude and petroleum metrics.
* **📊 Double-Chart Visualization:** Interactive, animated bar and doughnut charts displaying:
  * Commercial vs. SPR inventory ratios.
  * Joint weekly stock drawdowns.
  * International trade flow balances (Imports vs. Exports).
  * Domestic Crude Production vs. Refinery Runs vs. Product Demand.
* **🏛️ Historical Baselines:** Dashboards feature dashed reference lines comparing the active week against EIA all-time record thresholds (including the historic 6.44M b/d export record set the week of April 24, 2026).
* **⚡ Client-Side Exporting:** Directly export your filtered dataset to a clean CSV from your browser.
* **🔄 Reusable Pipeline:** Automated Python data pipeline that can ingest future weekly reports and update the dashboard in seconds.

---

## 📂 Project Architecture
```bash
├── process_oil_data.py       # Python pipeline: ingests raw table1.csv, cleans and exports JSON/CSV
├── build_dashboard.py        # Dashboard generator: compiles index.html with embedded dataset
├── table1.csv                # Raw EIA input spreadsheet (obtained from eia.gov)
├── filtered_crude_oil_data.csv # Polished, filtered output spreadsheet (Stocks & Flows)
├── oil_dashboard_data.json   # Cleaned JSON dataset loaded by the visual dashboard
└── index.html                # Premium client-side visual dashboard (open by double-clicking!)
```

---

## 🚀 Ingesting New Weekly Reports
When a new Weekly Petroleum Status Report is released by the EIA:
1. Go to the [EIA Weekly Petroleum Status Report page](https://www.eia.gov/petroleum/supply/weekly/).
2. Download the spreadsheet for **Table 1** (or table1.csv) and save it in this directory as `table1.csv`.
3. Run the automated pipeline:
   ```bash
   python process_oil_data.py
   python build_dashboard.py
   ```
4. Open or refresh `index.html` to see your updated interactive charts and tables instantly!

---

## 🛠️ Technology Stack
* **Core Logic:** Python (standard `csv`, `json`, `os` libraries)
* **Visual Interface:** HTML5, Premium Vanilla CSS (Glassmorphism, Dark Slate theme, custom animations)
* **Chart System:** [Chart.js](https://www.chartjs.org/) & [Chart.js Annotation Plugin](https://www.chartjs.org/chartjs-plugin-annotation/latest/) (loaded via CDN)
* **Fonts:** Outfit & Inter (loaded via Google Fonts)
