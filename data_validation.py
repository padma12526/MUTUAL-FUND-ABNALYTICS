import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("===== DATA VALIDATION =====")

# Missing values
print("\nMissing Values in Fund Master:")
print(fund_master.isnull().sum())

print("\nMissing Values in NAV History:")
print(nav_history.isnull().sum())

# Duplicate records
print("\nDuplicate Records in Fund Master:")
print(fund_master.duplicated().sum())

print("\nDuplicate Records in NAV History:")
print(nav_history.duplicated().sum())

# Compare scheme codes
if "scheme_code" in fund_master.columns and "scheme_code" in nav_history.columns:
    missing_codes = set(fund_master["scheme_code"]) - set(nav_history["scheme_code"])

    print("\nMissing Scheme Codes in NAV History:")
    print(missing_codes)

    print("\nTotal Missing Codes:", len(missing_codes))
else:
    print("\nColumn 'scheme_code' not found in one or both files.")