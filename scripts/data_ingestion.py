from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

csv_files = list(RAW_DIR.glob("*.csv"))

if not csv_files:
    print("No CSV files found in data/raw")

for file in csv_files:
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")

    try:
        df = pd.read_csv(file)

        print(f"Shape: {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")