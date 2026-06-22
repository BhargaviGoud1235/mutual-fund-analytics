import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"].astype(str))
nav_codes = set(nav_history["amfi_code"].astype(str))

missing_codes = master_codes - nav_codes

print(f"Total fund master codes: {len(master_codes)}")
print(f"Total NAV history codes: {len(nav_codes)}")
print(f"Missing codes: {len(missing_codes)}")