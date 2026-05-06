import os
import csv
import json

def clean_value(v):
    if not v:
        return 0.0
    # Remove quotes, spaces, commas, and handle special chars like ' ' or '-'
    v = v.replace('"', '').replace(',', '').strip()
    if v in ['', '-', ' ', '', '?', '_']:
        return 0.0
    try:
        return float(v)
    except ValueError:
        return v

def run_parser():
    csv_path = "c:/Users/17169/Desktop/Oil data/table1.csv"
    if not os.path.exists(csv_path):
        print("table1.csv not found!")
        return

    stocks = []
    flows = []

    current_section = "Stocks"
    
    with open(csv_path, "r", encoding="latin-1") as f:
        reader = csv.reader(f)
        row_list = list(reader)

    # First section headers (Stocks - Million Barrels)
    # Row 0: ["STUB_1","4/24/26","4/17/26","Difference","Percent Change","4/25/25","Difference","Percent Change"]
    header1 = [clean_value(x) for x in row_list[0]]
    dates1 = {
        "current": header1[1],
        "prior": header1[2],
        "year_ago": header1[5]
    }

    # Find the transition row (row 21 represents table 9/supply headers)
    transition_row_idx = -1
    for idx, row in enumerate(row_list):
        if idx > 0 and "Supply" in row[0] or "STUB_2" in row:
            transition_row_idx = idx
            break
        if idx > 0 and len(row) > 1 and "Domestic Production" in row[1]:
            transition_row_idx = idx - 1
            break

    if transition_row_idx == -1:
        transition_row_idx = 20 # Fallback

    # Parse Stocks (Rows 1 to transition_row_idx - 1)
    stocks_rows_to_keep = [
        "Crude Oil",
        "Commercial (Excluding SPR)",
        "Strategic Petroleum Reserve (SPR)",
        "Total Stocks (Including SPR)",
        "Total Stocks (Excluding SPR)"
    ]

    for idx in range(1, transition_row_idx):
        row = row_list[idx]
        if not row or not row[0].strip():
            continue
        name = row[0].replace('"', '').strip()
        if name in stocks_rows_to_keep:
            # Format row
            cleaned_row = {
                "metric": name,
                "current_week": clean_value(row[1]),
                "prior_week": clean_value(row[2]),
                "weekly_change": clean_value(row[3]),
                "weekly_pct_change": clean_value(row[4]),
                "year_ago": clean_value(row[5]),
                "yearly_change": clean_value(row[6]),
                "yearly_pct_change": clean_value(row[7]),
                "unit": "Million Barrels"
            }
            stocks.append(cleaned_row)

    # Parse Flows (Rows transition_row_idx + 1 onwards)
    # The columns for flows are:
    # 0: Section Name
    # 1: Item Name
    # 2: Current Week (4/24/26)
    # 3: Week Ago (4/17/26)
    # 4: Difference
    # 5: Year Ago (4/25/25)
    # 6: Difference (Yearly)
    # 7: 4-Week Average Current
    # 8: 4-Week Average Year Ago
    # 9: 4-Week Average % Change
    # 10: Cumulative Daily Average Current
    # 11: Cumulative Daily Average Year Ago
    # 12: Cumulative Daily Average % Change

    flow_rows_to_keep = [
        ("(1)     Domestic Production", "Crude Oil Production (Total)"),
        ("(2)        Alaska", "Crude Oil Production (Alaska)"),
        ("(3)        Lower 48", "Crude Oil Production (Lower 48)"),
        ("(4)     Transfers to Crude Oil Supply", "Transfers to Crude Oil Supply"),
        ("(7)     Net Imports (Including SPR)", "Net Crude Oil Imports (Incl. SPR)"),
        ("(8)        Imports", "Crude Oil Imports (Total)"),
        ("(9)            Commercial Crude Oil", "Commercial Crude Oil Imports"),
        ("(12)        Exports", "Crude Oil Exports (Total)"),
        ("(13)   Stock Change (+/build; -/draw)", "Crude Oil Stock Change Rate"),
        ("(14)       Commercial Stock Change", "Commercial Stock Change Rate"),
        ("(15)       SPR Stock Change", "SPR Stock Change Rate"),
        ("(16)   Adjustment", "Unaccounted Supply Adjustment"),
        ("(17)   Crude Oil Input to Refineries", "Refinery Crude Oil Inputs"),
        ("(30)   Total", "Total Petroleum Products Demand"),
        ("(33)   Total", "Net Total Petroleum Imports")
    ]

    for idx in range(transition_row_idx + 1, len(row_list)):
        row = row_list[idx]
        if len(row) < 13:
            continue
        section = row[0].replace('"', '').strip()
        item_raw = row[1].replace('"', '').strip()
        
        # Check if we should keep this row
        match_found = False
        display_name = ""
        for raw_name, clean_name in flow_rows_to_keep:
            if raw_name in item_raw:
                # Disambiguate Products Supplied "Total" vs Net Imports "Total"
                if raw_name == "(30)   Total" and "Products Supplied" not in section:
                    continue
                if raw_name == "(33)   Total" and "Net Imports" not in section:
                    continue
                match_found = True
                display_name = clean_name
                break
        
        if match_found:
            cleaned_row = {
                "section": section,
                "metric_raw": item_raw,
                "metric": display_name,
                "current_week": clean_value(row[2]),
                "prior_week": clean_value(row[3]),
                "weekly_change": clean_value(row[4]),
                "year_ago": clean_value(row[5]),
                "yearly_change": clean_value(row[6]),
                "avg_4wk_current": clean_value(row[7]),
                "avg_4wk_year_ago": clean_value(row[8]),
                "avg_4wk_pct_change": clean_value(row[9]),
                "cum_daily_current": clean_value(row[10]),
                "cum_daily_year_ago": clean_value(row[11]),
                "cum_daily_pct_change": clean_value(row[12]),
                "unit": "Thousand Barrels per Day"
            }
            flows.append(cleaned_row)

    # Output simplified CSV
    simplified_csv_path = "c:/Users/17169/Desktop/Oil data/filtered_crude_oil_data.csv"
    with open(simplified_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Section 1: Stocks
        writer.writerow(["SECTION 1: CRUDE OIL & PETROLEUM STOCK LEVELS (Inventories in Million Barrels)"])
        writer.writerow(["Metric", f"Current Week ({dates1['current']})", f"Week Ago ({dates1['prior']})", "Weekly Change", "Weekly % Change", f"Year Ago ({dates1['year_ago']})", "Yearly Change", "Yearly % Change"])
        for s in stocks:
            writer.writerow([
                s["metric"], s["current_week"], s["prior_week"], s["weekly_change"], s["weekly_pct_change"],
                s["year_ago"], s["yearly_change"], s["yearly_pct_change"]
            ])
        
        writer.writerow([])
        # Section 2: Flows
        writer.writerow(["SECTION 2: CRUDE OIL & PETROLEUM FLOWS (Rates in Thousand Barrels per Day)"])
        writer.writerow([
            "Metric", f"Current Week Flow", f"Week Ago Flow", "Weekly Change", f"Year Ago Flow", "Yearly Change",
            "4-Week Avg (Current)", "4-Week Avg (Year Ago)", "4-Week Avg % Change",
            "Cum. Daily Avg (Current)", "Cum. Daily Avg (Year Ago)", "Cum. Daily Avg % Change"
        ])
        for fl in flows:
            writer.writerow([
                fl["metric"], fl["current_week"], fl["prior_week"], fl["weekly_change"], fl["year_ago"], fl["yearly_change"],
                fl["avg_4wk_current"], fl["avg_4wk_year_ago"], fl["avg_4wk_pct_change"],
                fl["cum_daily_current"], fl["cum_daily_year_ago"], fl["cum_daily_pct_change"]
            ])

    print(f"Simplified CSV written to: {simplified_csv_path}")

    # Return data as dict
    data = {
        "dates": dates1,
        "stocks": stocks,
        "flows": flows
    }
    
    # Save as JSON
    with open("c:/Users/17169/Desktop/Oil data/oil_dashboard_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("JSON data written for web app!")

if __name__ == "__main__":
    run_parser()
