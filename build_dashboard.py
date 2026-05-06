import json
import os

def generate_html():
    json_path = "c:/Users/17169/Desktop/Oil data/oil_dashboard_data.json"
    if not os.path.exists(json_path):
        print("oil_dashboard_data.json not found!")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert data to JS object string
    data_js = json.dumps(data, indent=2)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weekly Petroleum Status Report Dashboard | Cleaned & Filtered</title>
    <meta name="description" content="A clean, interactive, and filtered dashboard summarizing the latest Weekly Petroleum Status Report (WPSR) focusing strictly on Oil, Crude Oil, and Petroleum metrics.">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@2.1.0/dist/chartjs-plugin-annotation.min.js"></script>
    <style>
        :root {{
            --bg-primary: #0b0f19;
            --bg-secondary: #111827;
            --bg-card: rgba(17, 24, 39, 0.7);
            --border-color: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(245, 158, 11, 0.4);
            
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --text-muted: #6b7280;
            
            --accent-gold: #f59e0b;
            --accent-gold-glowing: rgba(245, 158, 11, 0.15);
            --accent-blue: #3b82f6;
            --accent-emerald: #10b981;
            --accent-rose: #f43f5e;
            
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.15), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            --shadow-glass: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-primary);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            padding-bottom: 80px;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(245, 158, 11, 0.04) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(59, 130, 246, 0.05) 0%, transparent 50%);
            background-attachment: fixed;
            -webkit-font-smoothing: antialiased;
        }}

        /* Scrollbar styling */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: var(--bg-primary);
        }}
        ::-webkit-scrollbar-thumb {{
            background: #27272a;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #3f3f46;
        }}

        header {{
            background: rgba(11, 15, 25, 0.8);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 16px 5%;
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .logo-section {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .logo-icon {{
            background: linear-gradient(135deg, var(--accent-gold), #d97706);
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
            animation: pulse 3s infinite alternate;
        }}

        .logo-icon svg {{
            width: 20px;
            height: 20px;
            fill: #000;
        }}

        .logo-text h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 800;
            background: linear-gradient(to right, #ffffff, #e5e7eb, var(--accent-gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }}

        .logo-text p {{
            font-size: 0.75rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .header-meta {{
            text-align: right;
        }}

        .header-meta .date-label {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .header-meta .date-value {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--accent-gold);
        }}

        main {{
            max-width: 1400px;
            margin: 40px auto 0;
            padding: 0 24px;
        }}

        /* Welcome Section */
        .welcome-card {{
            background: var(--bg-card);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-glass);
            position: relative;
            overflow: hidden;
        }}

        .welcome-card::after {{
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 250px;
            height: 250px;
            background: radial-gradient(circle, rgba(245, 158, 11, 0.08) 0%, transparent 70%);
            pointer-events: none;
        }}

        .welcome-card h2 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 12px;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .welcome-card p {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            max-width: 1000px;
            margin-bottom: 20px;
        }}

        .badge {{
            display: inline-flex;
            align-items: center;
            padding: 6px 12px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border: 1px solid transparent;
        }}

        .badge-amber {{
            background: rgba(245, 158, 11, 0.1);
            color: var(--accent-gold);
            border-color: rgba(245, 158, 11, 0.2);
        }}

        .badge-blue {{
            background: rgba(59, 130, 246, 0.1);
            color: #60a5fa;
            border-color: rgba(59, 130, 246, 0.2);
        }}

        /* Key Highlights Grid */
        .highlights-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}

        .highlight-card {{
            background: var(--bg-card);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            box-shadow: var(--shadow-md);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}

        .highlight-card:hover {{
            transform: translateY(-4px);
            border-color: var(--border-hover);
            box-shadow: 0 12px 24px rgba(245, 158, 11, 0.08);
        }}

        .highlight-card::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--accent-gold);
            opacity: 0.5;
        }}

        .highlight-card.draw::before {{
            background: var(--accent-rose);
        }}

        .highlight-card.build::before {{
            background: var(--accent-emerald);
        }}

        .highlight-card .card-title {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
            font-weight: 500;
        }}

        .highlight-card .card-value-group {{
            display: flex;
            align-items: baseline;
            gap: 12px;
            margin-bottom: 6px;
        }}

        .highlight-card .card-value {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -1px;
        }}

        .highlight-card .card-unit {{
            font-size: 0.85rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .highlight-card .card-change {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.85rem;
            font-weight: 600;
        }}

        .highlight-card.draw .card-change {{
            color: var(--accent-rose);
        }}

        .highlight-card.build .card-change {{
            color: var(--accent-emerald);
        }}

        .highlight-card .card-subtitle {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 6px;
        }}

        /* Navigation Tabs */
        .tabs-nav {{
            display: flex;
            gap: 8px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 30px;
            padding-bottom: 12px;
            overflow-x: auto;
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 10px 20px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.95rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .tab-btn:hover {{
            color: #ffffff;
            background: rgba(255, 255, 255, 0.04);
        }}

        .tab-btn.active {{
            color: #000000;
            background: var(--accent-gold);
            box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
        }}

        .tab-content {{
            display: none;
            animation: fadeIn 0.4s ease-out;
        }}

        .tab-content.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Dashboard Overview Grid */
        .dashboard-grid {{
            display: grid;
            grid-template-columns: 3fr 2fr;
            gap: 30px;
            margin-bottom: 40px;
        }}

        @media (max-width: 1024px) {{
            .dashboard-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .panel {{
            background: var(--bg-card);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 24px;
            box-shadow: var(--shadow-lg);
            height: 100%;
        }}

        .panel-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 12px;
        }}

        .panel-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        /* Textual Analysis Styles */
        .insight-section {{
            margin-bottom: 24px;
        }}

        .insight-section h4 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: var(--accent-gold);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .insight-section p {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-bottom: 16px;
            text-align: justify;
        }}

        .bullets-list {{
            list-style: none;
            margin-bottom: 16px;
        }}

        .bullets-list li {{
            position: relative;
            padding-left: 20px;
            margin-bottom: 8px;
            font-size: 0.95rem;
            color: var(--text-secondary);
        }}

        .bullets-list li::before {{
            content: 'â¢';
            position: absolute;
            left: 6px;
            color: var(--accent-gold);
            font-size: 1.25rem;
            top: -2px;
        }}

        /* Tables */
        .table-container {{
            width: 100%;
            overflow-x: auto;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            margin-bottom: 20px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.9rem;
        }}

        th {{
            background: #181d2a;
            color: var(--text-primary);
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-color);
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            white-space: nowrap;
        }}

        td {{
            padding: 14px 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            color: var(--text-secondary);
            white-space: nowrap;
        }}

        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
            color: #ffffff;
        }}

        td.metric-name {{
            font-weight: 600;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
        }}

        .val-draw {{
            color: #fb7185 !important;
            font-weight: 600;
        }}

        .val-build {{
            color: #34d399 !important;
            font-weight: 600;
        }}

        .val-steady {{
            color: var(--text-muted);
        }}

        /* Buttons & Actions */
        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #1f2937;
            color: #ffffff;
            border: 1px solid var(--border-color);
            padding: 10px 18px;
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            text-decoration: none;
        }}

        .btn:hover {{
            background: #374151;
            border-color: var(--accent-gold);
            box-shadow: 0 4px 12px rgba(245, 158, 11, 0.1);
        }}

        .btn-primary {{
            background: var(--accent-gold);
            color: #000000;
            border: none;
        }}

        .btn-primary:hover {{
            background: #fbbf24;
            box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4);
        }}

        .download-panel {{
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(59, 130, 246, 0.05) 100%);
            border: 1px solid rgba(245, 158, 11, 0.2);
            border-radius: 16px;
            padding: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 30px;
        }}

        @media (max-width: 768px) {{
            .download-panel {{
                flex-direction: column;
                gap: 16px;
                text-align: center;
            }}
        }}

        .download-text h3 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 4px;
            color: #ffffff;
        }}

        .download-text p {{
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}

        /* Animations */
        @keyframes pulse {{
            0% {{ box-shadow: 0 0 15px rgba(245, 158, 11, 0.3); }}
            100% {{ box-shadow: 0 0 25px rgba(245, 158, 11, 0.6); }}
        }}

        .chart-container {{
            position: relative;
            width: 100%;
            height: 350px;
        }}

        .flex-row-sb {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .pill-toggle {{
            display: flex;
            background: #181d2a;
            border: 1px solid var(--border-color);
            padding: 4px;
            border-radius: 8px;
            gap: 2px;
        }}

        .pill-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 6px 12px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            border-radius: 6px;
            transition: all 0.2s;
        }}

        .pill-btn.active {{
            background: #2d3748;
            color: #ffffff;
        }}

        .trend-badge {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
        }}

        .trend-badge.down {{
            background: rgba(244, 63, 94, 0.15);
            color: var(--accent-rose);
        }}

        .trend-badge.up {{
            background: rgba(16, 185, 129, 0.15);
            color: var(--accent-emerald);
        }}
    </style>
</head>
<body>

    <header>
        <div class="logo-section">
            <div class="logo-icon">
                <svg viewBox="0 0 24 24">
                    <path d="M12,3C12,3 6,10 6,14C6,17.31 8.69,20 12,20C15.31,20 18,17.31 18,14C18,10 12,3 12,3M12,18C9.79,18 8,16.21 8,14C8,12.5 9.17,10.24 12,6.85C14.83,10.24 16,12.5 16,14C16,16.21 14.21,18 12,18Z"/>
                </svg>
            </div>
            <div class="logo-text">
                <h1>WEEKLY PETROLEUM STATUS REPORT</h1>
                <p>Cleaned Crude Oil & Petroleum Analytics</p>
            </div>
        </div>
        <div class="header-meta">
            <div class="date-label">Week Ending Date</div>
            <div class="date-value">{data['dates']['current']}</div>
        </div>
    </header>

    <main>
        <!-- Welcome Card -->
        <div class="welcome-card">
            <h2>
                <span style="color: var(--accent-gold);">â¡</span> Cleaned & Filtered Report Dashboard
            </h2>
            <p>
                We have processed the dense EIA Weekly Petroleum Status Report (WPSR) spreadsheet to filter out irrelevant or confusing non-petroleum rows (like biofuels, NGLs, oxygenates, and other alcohols). What remains is a crystal-clear, focused view of the global core market drivers: <strong>Crude Oil Inventories, Domestic Supply, Import/Export Flows, and Refinery Runs</strong>.
            </p>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <span class="badge badge-amber">Filtered Core: Crude Oil & Petroleum Only</span>
                <span class="badge badge-blue">Reorganized structure: Stock Levels separated from Flows</span>
                <span class="badge badge-amber" style="background: rgba(16, 185, 129, 0.1); color: var(--accent-emerald); border-color: rgba(16, 185, 129, 0.2);">Data Ending: {data['dates']['current']}</span>
            </div>
        </div>

        <!-- Highlights Grid -->
        <div class="highlights-grid">
            <!-- Commercial Stocks -->
            <div class="highlight-card draw">
                <div class="card-title">Commercial Crude Stocks</div>
                <div class="card-value-group">
                    <div class="card-value">459.5</div>
                    <div class="card-unit">Million bbls</div>
                </div>
                <div class="card-change">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                        <path d="M12 5v14M19 12l-7 7-7-7"/>
                    </svg>
                    <span>6.23M bbls (-1.3%)</span>
                </div>
                <div class="card-subtitle">Excluding Strategic Petroleum Reserve (SPR)</div>
            </div>

            <!-- SPR Stocks -->
            <div class="highlight-card draw">
                <div class="card-title">SPR Crude Stocks</div>
                <div class="card-value-group">
                    <div class="card-value">397.9</div>
                    <div class="card-unit">Million bbls</div>
                </div>
                <div class="card-change">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                        <path d="M12 5v14M19 12l-7 7-7-7"/>
                    </svg>
                    <span>7.12M bbls (-1.8%)</span>
                </div>
                <div class="card-subtitle">Strategic Petroleum Reserve Drawdown</div>
            </div>

            <!-- Crude Production -->
            <div class="highlight-card build">
                <div class="card-title">Domestic Crude Production</div>
                <div class="card-value-group">
                    <div class="card-value">13,586</div>
                    <div class="card-unit">Thousand b/d</div>
                </div>
                <div class="card-change">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                        <path d="M12 19V5M5 12l7-7 7 7"/>
                    </svg>
                    <span>+1 kb/d (+0.0%)</span>
                </div>
                <div class="card-subtitle">Lower 48: 13,161 | Alaska: 425</div>
            </div>

            <!-- Net Imports -->
            <div class="highlight-card draw">
                <div class="card-title">Net Crude Imports</div>
                <div class="card-value-group">
                    <div class="card-value">-688</div>
                    <div class="card-unit">Thousand b/d</div>
                </div>
                <div class="card-change">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                        <path d="M12 5v14M19 12l-7 7-7-7"/>
                    </svg>
                    <span>-1.97M b/d (Net Exporter!)</span>
                </div>
                <div class="card-subtitle">Imports: 5,750 kb/d | Exports: 6,438 kb/d</div>
            </div>
        </div>

        <!-- Navigation Tabs -->
        <div class="tabs-nav">
            <button class="tab-btn active" onclick="switchTab('tab-insights')">
                <span style="font-size: 1.1rem;">ð</span> Executive Insights
            </button>
            <button class="tab-btn" onclick="switchTab('tab-stocks')">
                <span style="font-size: 1.1rem;">ð</span> Inventories (Stocks)
            </button>
            <button class="tab-btn" onclick="switchTab('tab-flows')">
                <span style="font-size: 1.1rem;">ð</span> Daily Flow Rates
            </button>
            <button class="tab-btn" onclick="switchTab('tab-table')">
                <span style="font-size: 1.1rem;">ð</span> Filtered Spreadsheet Table
            </button>
        </div>

        <!-- TAB 1: EXECUTIVE INSIGHTS -->
        <div id="tab-insights" class="tab-content active">
            <div class="dashboard-grid">
                <!-- Left panel: Textual Analysis -->
                <div class="panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>ð</span> Weekly Executive Briefing
                        </div>
                    </div>
                    <div class="insight-section">
                        <h4>â The Big Picture: Massive Drawdown</h4>
                        <p>
                            For the week ending <strong>{data['dates']['current']}</strong>, the U.S. crude oil supply-demand balance experienced a highly bullish tightening. Combined crude inventories (Commercial + SPR) contracted by a massive <strong>13.35 million barrels</strong> in a single week. If we factor in refined petroleum products, the total petroleum stocks collapsed by <strong>24.08 million barrels</strong>, pointing to an extremely active refining segment and highly robust domestic and international product consumption.
                        </p>
                    </div>

                    <div class="insight-section">
                        <h4>â The Export Surge & Net Exporter Transition</h4>
                        <p>
                            A key catalyst behind this dramatic stockpile erosion was a huge surge in international shipments. U.S. crude oil exports skyrocketed by <strong>1.64 million barrels per day (b/d)</strong> to reach an average of <strong>6.438 million b/d</strong>. At the same time, crude oil imports decreased by <strong>329,000 b/d</strong> to average 5.750 million b/d.
                        </p>
                        <p>
                            This physical mismatch propelled the United States into a massive <strong>net crude exporter</strong> stance, with net imports landing at <strong>-688,000 b/d</strong> (compared to being a net importer of +1.280 million b/d the prior week)—representing a massive swing of <strong>1.969 million b/d</strong> of crude out of the domestic system.
                        </p>
                    </div>

                    <div class="insight-section">
                        <h4>ð Production Steady & Refining Operating High</h4>
                        <p>
                            Domestic crude oil production hovered virtually flat, gaining just 1,000 b/d to average <strong>13.586 million b/d</strong> (Lower 48 states contributed 13.161 million b/d, while Alaska contributed 425,000 b/d). Refiners, however, stepped up operations to digest inventories, with daily inputs to refineries rising by <strong>85,000 b/d</strong> to average <strong>16.071 million b/d</strong>. This indicates high refinery utilization rates to support summer demand.
                        </p>
                    </div>

                    <div class="insight-section">
                        <h4>ð¥ Exploding Demand for Petroleum Products</h4>
                        <p>
                            Total product supplied—EIA's proxy for implied consumer demand—surged by <strong>1.433 million b/d</strong>, bringing total U.S. petroleum product demand to <strong>21.131 million b/d</strong>. This surge shows that physical consumption of motor gasoline (which edged up slightly to 9.104 million b/d), diesel/distillate fuels, and heating oil is heavily drawing on refined inventories.
                        </p>
                    </div>
                </div>

                <!-- Right panel: Quick Charts -->
                <div class="panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>ð</span> Inventory Allocation
                        </div>
                    </div>
                    <div class="chart-container">
                        <canvas id="stocksChart"></canvas>
                    </div>
                    <div style="margin-top: 24px;">
                        <h4 style="font-family:'Outfit', sans-serif; font-size:1rem; color:var(--accent-gold); margin-bottom:8px;">KEY INVENTORY RATIOS</h4>
                        <ul class="bullets-list" style="font-size:0.85rem;">
                            <li><strong>Commercial Reserves</strong> constitute <strong>53.6%</strong> of total U.S. crude stocks.</li>
                            <li><strong>Strategic Petroleum Reserve (SPR)</strong> holds the remaining <strong>46.4%</strong>.</li>
                            <li>Weekly commercial drawdown was <strong>1.3%</strong>, while SPR dropped by <strong>1.8%</strong>.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: INVENTORIES (STOCKS) -->
        <div id="tab-stocks" class="tab-content">
            <div class="dashboard-grid" style="grid-template-columns: 1fr 1fr;">
                <div class="panel">
                    <div class="panel-header">
                        <div class="panel-title">ð Core Stock Levels (Million Barrels)</div>
                    </div>
                    <div class="table-container">
                        <table id="stocksTable">
                            <thead>
                                <tr>
                                    <th>Metric</th>
                                    <th>Current Week</th>
                                    <th>Week Ago</th>
                                    <th>Weekly Change</th>
                                    <th>% Change</th>
                                    <th>Year Ago</th>
                                </tr>
                            </thead>
                            <tbody id="stocksTableBody">
                                <!-- Populated dynamically by JS -->
                            </tbody>
                        </table>
                    </div>
                    <div style="font-size:0.8rem; color:var(--text-muted); margin-top:8px;">
                        * Total Stocks (Excluding SPR) represents commercial inventories held at refineries, pipelines, and bulk terminals.
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">
                        <div class="panel-title">ð Stock Changes Visualized</div>
                    </div>
                    <div class="chart-container" style="height: 380px;">
                        <canvas id="stockChangesChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 3: DAILY FLOW RATES -->
        <div id="tab-flows" class="tab-content">
            <div class="panel" style="margin-bottom: 30px;">
                <div class="panel-header">
                    <div class="panel-title">ð Daily Crude & Product Flow Rates (Thousand Barrels per Day)</div>
                </div>
                <div class="table-container">
                    <table id="flowsTable">
                        <thead>
                            <tr>
                                <th>Metric</th>
                                <th>Current Flow</th>
                                <th>Week Ago</th>
                                <th>Change</th>
                                <th>Year Ago</th>
                                <th>4-Week Avg</th>
                                <th>Year Ago 4-Wk Avg</th>
                                <th>4-Wk Change %</th>
                            </tr>
                        </thead>
                        <tbody id="flowsTableBody">
                            <!-- Populated dynamically by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div class="dashboard-grid" style="grid-template-columns: 1fr 1fr;">
                <div class="panel">
                    <div class="panel-header">
                        <div class="panel-title">ð Trade Flow Balance (kb/d)</div>
                    </div>
                    <div class="chart-container">
                        <canvas id="tradeFlowChart"></canvas>
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">
                        <div class="panel-title">ð Supply & Refining Rates (kb/d)</div>
                    </div>
                    <div class="chart-container">
                        <canvas id="productionRefiningChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 4: FILTERED SPREADSHEET TABLE -->
        <div id="tab-table" class="tab-content">
            <div class="panel">
                <div class="panel-header flex-row-sb">
                    <div class="panel-title">ð Filtered Master Oil Spreadsheet</div>
                    <div style="display:flex; gap:10px;">
                        <input type="text" id="tableSearch" placeholder="Search metrics..." oninput="filterMasterTable()" style="background:#181d2a; border:1px solid var(--border-color); border-radius:6px; color:#fff; padding:6px 12px; font-size:0.85rem;">
                        <button class="btn btn-primary" onclick="exportFilteredCSV()" style="padding:6px 14px; font-size:0.8rem;">
                            ð¥ Export Clean CSV
                        </button>
                    </div>
                </div>
                <div class="table-container">
                    <table id="masterTable">
                        <thead>
                            <tr>
                                <th>Type</th>
                                <th>Metric</th>
                                <th>Current Value</th>
                                <th>Week Ago</th>
                                <th>Weekly Change</th>
                                <th>Weekly Change %</th>
                                <th>Year Ago</th>
                                <th>Unit</th>
                            </tr>
                        </thead>
                        <tbody id="masterTableBody">
                            <!-- Populated dynamically by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Download Section -->
        <div class="download-panel">
            <div class="download-text">
                <h3>ð¥ Download Simplified Spreadsheet</h3>
                <p>We have generated a clean, standardized, and professionally structured CSV containing ONLY these filtered oil metrics.</p>
            </div>
            <div style="display:flex; gap:12px;">
                <a href="filtered_crude_oil_data.csv" class="btn" download="filtered_crude_oil_data.csv">
                    ð Download Filtered CSV
                </a>
                <button class="btn btn-primary" onclick="switchTab('tab-table')">
                    ð View in Browser
                </button>
            </div>
        </div>

    </main>

    <script>
        // Embed the processed EIA data
        const eiaData = {data_js};

        // Tab Switching Logic
        function switchTab(tabId) {{
            // Hide all tabs
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => content.classList.remove('active'));

            // Deactivate all tab buttons
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => btn.classList.remove('active'));

            // Show active tab
            document.getElementById(tabId).classList.add('active');

            // Find current button and set active
            const clickedBtn = Array.from(buttons).find(btn => btn.getAttribute('onclick').includes(tabId));
            if (clickedBtn) clickedBtn.classList.add('active');

            // Re-render charts on tab switch if needed (fixes Chart.js rendering in hidden div bug)
            if (tabId === 'tab-stocks') {{
                initStocksTabCharts();
            }} else if (tabId === 'tab-flows') {{
                initFlowsTabCharts();
            }}
        }}

        // Format helpers
        function fmtVal(val, unit) {{
            if (val === null || val === undefined || isNaN(val)) return '-';
            const sign = val > 0 ? '+' : '';
            return val.toLocaleString(undefined, {{ minimumFractionDigits: 1, maximumFractionDigits: 2 }});
        }}

        function fmtChange(val, isPct = false) {{
            if (val === null || val === undefined || isNaN(val) || val === 0) return `<span class="val-steady">0.0${{isPct ? '%' : ''}}</span>`;
            const sign = val > 0 ? '+' : '';
            const cls = val > 0 ? 'val-build' : 'val-draw';
            return `<span class="${{cls}}">${{sign}}${{val.toLocaleString(undefined, {{ minimumFractionDigits: 1, maximumFractionDigits: 2 }})}}${{isPct ? '%' : ''}}</span>`;
        }}

        // Load Tables
        function loadStocksTable() {{
            const tbody = document.getElementById('stocksTableBody');
            tbody.innerHTML = '';
            eiaData.stocks.forEach(s => {{
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="metric-name">${{s.metric}}</td>
                    <td>${{fmtVal(s.current_week)}}</td>
                    <td>${{fmtVal(s.prior_week)}}</td>
                    <td>${{fmtChange(s.weekly_change)}}</td>
                    <td>${{fmtChange(s.weekly_pct_change, true)}}</td>
                    <td>${{fmtVal(s.year_ago)}}</td>
                `;
                tbody.appendChild(row);
            }});
        }}

        function loadFlowsTable() {{
            const tbody = document.getElementById('flowsTableBody');
            tbody.innerHTML = '';
            eiaData.flows.forEach(fl => {{
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="metric-name">${{fl.metric}}</td>
                    <td>${{fmtVal(fl.current_week)}}</td>
                    <td>${{fmtVal(fl.prior_week)}}</td>
                    <td>${{fmtChange(fl.weekly_change)}}</td>
                    <td>${{fmtVal(fl.year_ago)}}</td>
                    <td>${{fmtVal(fl.avg_4wk_current)}}</td>
                    <td>${{fmtVal(fl.avg_4wk_year_ago)}}</td>
                    <td>${{fmtChange(fl.avg_4wk_pct_change, true)}}</td>
                `;
                tbody.appendChild(row);
            }});
        }}

        function loadMasterTable() {{
            const tbody = document.getElementById('masterTableBody');
            tbody.innerHTML = '';
            
            // Add Stocks
            eiaData.stocks.forEach(s => {{
                const row = document.createElement('tr');
                row.className = 'row-stocks';
                row.innerHTML = `
                    <td><span class="trend-badge" style="background:rgba(59,130,246,0.15); color:#60a5fa;">Inventory</span></td>
                    <td class="metric-name">${{s.metric}}</td>
                    <td>${{fmtVal(s.current_week)}}</td>
                    <td>${{fmtVal(s.prior_week)}}</td>
                    <td>${{fmtChange(s.weekly_change)}}</td>
                    <td>${{fmtChange(s.weekly_pct_change, true)}}</td>
                    <td>${{fmtVal(s.year_ago)}}</td>
                    <td>${{s.unit}}</td>
                `;
                tbody.appendChild(row);
            }});

            // Add Flows
            eiaData.flows.forEach(fl => {{
                const row = document.createElement('tr');
                row.className = 'row-flows';
                row.innerHTML = `
                    <td><span class="trend-badge" style="background:rgba(245,158,11,0.15); color:var(--accent-gold);">Daily Flow</span></td>
                    <td class="metric-name">${{fl.metric}}</td>
                    <td>${{fmtVal(fl.current_week)}}</td>
                    <td>${{fmtVal(fl.prior_week)}}</td>
                    <td>${{fmtChange(fl.weekly_change)}}</td>
                    <td>${{fmtChange((fl.weekly_change / (fl.prior_week || 1)) * 100, true)}}</td>
                    <td>${{fmtVal(fl.year_ago)}}</td>
                    <td>${{fl.unit}}</td>
                `;
                tbody.appendChild(row);
            }});
        }}

        function filterMasterTable() {{
            const query = document.getElementById('tableSearch').value.toLowerCase();
            const rows = document.getElementById('masterTableBody').getElementsByTagName('tr');
            Array.from(rows).forEach(row => {{
                const text = row.innerText.toLowerCase();
                if (text.includes(query)) {{
                    row.style.display = '';
                }} else {{
                    row.style.display = 'none';
                }}
            }});
        }}

        // Charts Initialization
        let stocksChartObj = null;
        let stockChangesChartObj = null;
        let tradeFlowChartObj = null;
        let productionRefiningChartObj = null;

        function initOverviewChart() {{
            const commercial = eiaData.stocks.find(s => s.metric.includes("Commercial")).current_week;
            const spr = eiaData.stocks.find(s => s.metric.includes("Strategic")).current_week;

            const ctx = document.getElementById('stocksChart').getContext('2d');
            if (stocksChartObj) stocksChartObj.destroy();
            
            stocksChartObj = new Chart(ctx, {{
                type: 'doughnut',
                data: {{
                    labels: ['Commercial Stocks', 'Strategic Petroleum Reserve (SPR)'],
                    datasets: [{{
                        data: [commercial, spr],
                        backgroundColor: ['#f59e0b', '#3b82f6'],
                        borderColor: '#111827',
                        borderWidth: 2,
                        hoverOffset: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'bottom',
                            labels: {{
                                color: '#f3f4f6',
                                font: {{ family: 'Outfit', size: 12 }}
                            }}
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return ` ${{context.label}}: ${{context.raw.toLocaleString()}} Million Barrels`;
                                }}
                            }}
                        }}
                    }}
                }}
            }});
        }}

        function initStocksTabCharts() {{
            const labels = eiaData.stocks.map(s => s.metric);
            const changes = eiaData.stocks.map(s => s.weekly_change);
            const colors = changes.map(v => v > 0 ? 'rgba(16, 185, 129, 0.7)' : 'rgba(244, 63, 94, 0.7)');
            const borderColors = changes.map(v => v > 0 ? '#10b981' : '#f43f5e');

            const ctx = document.getElementById('stockChangesChart').getContext('2d');
            if (stockChangesChartObj) stockChangesChartObj.destroy();

            stockChangesChartObj = new Chart(ctx, {{
                type: 'bar',
                data: {{
                    labels: labels,
                    datasets: [{{
                        label: 'Weekly Change (Million Barrels)',
                        data: changes,
                        backgroundColor: colors,
                        borderColor: borderColors,
                        borderWidth: 1.5,
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        x: {{
                            grid: {{ display: false }},
                            ticks: {{
                                color: '#9ca3af',
                                font: {{ family: 'Outfit', size: 10 }}
                            }}
                        }},
                        y: {{
                            grid: {{ color: 'rgba(255,255,255,0.05)' }},
                            ticks: {{
                                color: '#9ca3af',
                                font: {{ family: 'Outfit', size: 11 }}
                            }}
                        }}
                    }},
                    plugins: {{
                        legend: {{ display: false }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return ` Weekly Change: ${{context.raw > 0 ? '+' : ''}}${{context.raw.toFixed(3)}} Million bbls`;
                                }}
                            }}
                        }},
                        annotation: {{
                            annotations: {{
                                recordDrawLine: {{
                                    type: 'line',
                                    yMin: -17.05,
                                    yMax: -17.05,
                                    borderColor: 'rgba(244, 63, 94, 0.45)',
                                    borderWidth: 1.5,
                                    borderDash: [6, 4],
                                    label: {{
                                        content: 'All-Time Peak Commercial Draw: -17.05M (July 2023)',
                                        enabled: true,
                                        position: 'start',
                                        backgroundColor: 'rgba(15, 23, 42, 0.85)',
                                        color: '#fda4af',
                                        font: {{ family: 'Outfit', size: 9, weight: 'bold' }},
                                        padding: 4
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }});
        }}

        function initFlowsTabCharts() {{
            // Chart 1: Trade Balance
            const imports = eiaData.flows.find(f => f.metric === "Crude Oil Imports (Total)").current_week;
            const exports = eiaData.flows.find(f => f.metric === "Crude Oil Exports (Total)").current_week;
            const netImports = eiaData.flows.find(f => f.metric === "Net Crude Oil Imports (Incl. SPR)").current_week;

            const ctx1 = document.getElementById('tradeFlowChart').getContext('2d');
            if (tradeFlowChartObj) tradeFlowChartObj.destroy();

            tradeFlowChartObj = new Chart(ctx1, {{
                type: 'bar',
                data: {{
                    labels: ['Imports', 'Exports', 'Net Imports'],
                    datasets: [{{
                        label: 'Current Week Daily Flow (kb/d)',
                        data: [imports, exports, netImports],
                        backgroundColor: ['#3b82f6', '#f59e0b', netImports > 0 ? 'rgba(16, 185, 129, 0.7)' : 'rgba(244, 63, 94, 0.7)'],
                        borderColor: ['#2563eb', '#d97706', netImports > 0 ? '#10b981' : '#f43f5e'],
                        borderWidth: 1.5,
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        x: {{ grid: {{ display: false }}, ticks: {{ color: '#9ca3af', font: {{ family: 'Outfit' }} }} }},
                        y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9ca3af', font: {{ family: 'Outfit' }} }} }}
                    }},
                    plugins: {{ 
                        legend: {{ display: false }},
                        annotation: {{
                            annotations: {{
                                recordExportLine: {{
                                    type: 'line',
                                    yMin: 6438,
                                    yMax: 6438,
                                    borderColor: 'rgba(245, 158, 11, 0.65)',
                                    borderWidth: 1.5,
                                    borderDash: [5, 5],
                                    label: {{
                                        content: 'All-Time U.S. Crude Export Record: 6,438 kb/d (Set This Week!)',
                                        enabled: true,
                                        position: 'center',
                                        backgroundColor: 'rgba(15, 23, 42, 0.95)',
                                        color: '#fef08a',
                                        font: {{ family: 'Outfit', size: 9, weight: 'bold' }},
                                        padding: 4
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }});

            // Chart 2: Production & Refinery Inputs
            const prod = eiaData.flows.find(f => f.metric === "Crude Oil Production (Total)").current_week;
            const refinery = eiaData.flows.find(f => f.metric === "Refinery Crude Oil Inputs").current_week;
            const demand = eiaData.flows.find(f => f.metric === "Total Petroleum Products Demand").current_week;

            const ctx2 = document.getElementById('productionRefiningChart').getContext('2d');
            if (productionRefiningChartObj) productionRefiningChartObj.destroy();

            productionRefiningChartObj = new Chart(ctx2, {{
                type: 'bar',
                data: {{
                    labels: ['Crude Production', 'Refinery Inputs', 'Total Product Demand'],
                    datasets: [{{
                        label: 'Current Week Daily Flow (kb/d)',
                        data: [prod, refinery, demand],
                        backgroundColor: ['#10b981', '#3b82f6', '#8b5cf6'],
                        borderColor: ['#059669', '#2563eb', '#7c3aed'],
                        borderWidth: 1.5,
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        x: {{ grid: {{ display: false }}, ticks: {{ color: '#9ca3af', font: {{ family: 'Outfit' }} }} }},
                        y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#9ca3af', font: {{ family: 'Outfit' }} }} }}
                    }},
                    plugins: {{ 
                        legend: {{ display: false }},
                        annotation: {{
                            annotations: {{
                                recordProdLine: {{
                                    type: 'line',
                                    yMin: 13862,
                                    yMax: 13862,
                                    borderColor: 'rgba(16, 185, 129, 0.45)',
                                    borderWidth: 1.5,
                                    borderDash: [5, 5],
                                    label: {{
                                        content: 'All-Time U.S. Crude Production Record: 13,862 kb/d (Nov 2025)',
                                        enabled: true,
                                        position: 'start',
                                        backgroundColor: 'rgba(15, 23, 42, 0.85)',
                                        color: '#a7f3d0',
                                        font: {{ family: 'Outfit', size: 9, weight: 'bold' }},
                                        padding: 4
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }});
        }}

        // Dynamic CSV Exporter (creates and downloads on client side)
        function exportFilteredCSV() {{
            let csvContent = "data:text/csv;charset=utf-8,";
            
            // Section 1 Stocks
            csvContent += "SECTION 1: CRUDE OIL & PETROLEUM STOCK LEVELS (Inventories in Million Barrels)\\n";
            csvContent += "Metric,Current Week (${{eiaData.dates.current}}),Week Ago (${{eiaData.dates.prior}}),Weekly Change,Weekly % Change,Year Ago (${{eiaData.dates.year_ago}})\\n";
            eiaData.stocks.forEach(s => {{
                csvContent += `"${{s.metric}}",${{s.current_week}},${{s.prior_week}},${{s.weekly_change}},${{s.weekly_pct_change}},${{s.year_ago}}\\n`;
            }});
            
            csvContent += "\\n";
            
            // Section 2 Flows
            csvContent += "SECTION 2: CRUDE OIL & PETROLEUM FLOWS (Rates in Thousand Barrels per Day)\\n";
            csvContent += "Metric,Current Flow,Week Ago Flow,Weekly Change,Year Ago Flow,4-Week Avg Current,4-Week Avg Year Ago,4-Wk Avg Change %\\n";
            eiaData.flows.forEach(f => {{
                csvContent += `"${{f.metric}}",${{f.current_week}},${{f.prior_week}},${{f.weekly_change}},${{f.year_ago}},${{f.avg_4wk_current}},${{f.avg_4wk_year_ago}},${{f.avg_4wk_pct_change}}\\n`;
            }});

            const encodedUri = encodeURI(csvContent);
            const link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", "filtered_crude_oil_data.csv");
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}

        // Run on load
        window.addEventListener('DOMContentLoaded', () => {{
            loadStocksTable();
            loadFlowsTable();
            loadMasterTable();
            initOverviewChart();
        }});
    </script>
</body>
</html>
"""

    output_path = "c:/Users/17169/Desktop/Oil data/index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Stunning Web Dashboard written to: {output_path}")

if __name__ == "__main__":
    generate_html()
