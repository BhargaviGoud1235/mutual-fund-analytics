import requests
import pandas as pd
from pathlib import Path

schemes = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

output_dir = Path("data/raw/live_nav")
output_dir.mkdir(parents=True, exist_ok=True)

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df["scheme_code"] = scheme_code
        nav_df["scheme_name"] = data["meta"]["scheme_name"]

        output_file = output_dir / f"{scheme_name}.csv"
        nav_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"Error fetching {scheme_name} ({scheme_code}): {e}")