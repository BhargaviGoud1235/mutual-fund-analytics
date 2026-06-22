import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nColumns:")
print(df.columns.tolist())

print("\nNumber of unique fund houses:")
print(df["fund_house"].nunique())

print("\nFund houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub-categories:")
print(df["sub_category"].unique())

print("\nRisk categories:")
print(df["risk_category"].unique())

print("\nSample data:")
print(df.head())