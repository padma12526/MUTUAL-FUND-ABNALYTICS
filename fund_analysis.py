import pandas as pd

# Load fund master dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\n===== FUND MASTER ANALYSIS =====\n")

# Basic information
print("Shape:", fund_master.shape)

print("\nColumns:")
print(fund_master.columns)

print("\nData Types:")
print(fund_master.dtypes)

print("\nFirst 5 Rows:")
print(fund_master.head())

# Missing values
print("\nMissing Values:")
print(fund_master.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(fund_master.duplicated().sum())

# Print unique values (only if the column exists)
if "fund_house" in fund_master.columns:
    print("\nUnique Fund Houses:")
    print(fund_master["fund_house"].unique())
else:
    print("\nColumn 'fund_house' not found.")

if "category" in fund_master.columns:
    print("\nUnique Categories:")
    print(fund_master["category"].unique())
else:
    print("\nColumn 'category' not found.")

if "sub_category" in fund_master.columns:
    print("\nUnique Sub-Categories:")
    print(fund_master["sub_category"].unique())
else:
    print("\nColumn 'sub_category' not found.")

if "risk_grade" in fund_master.columns:
    print("\nUnique Risk Grades:")
    print(fund_master["risk_grade"].unique())
else:
    print("\nColumn 'risk_grade' not found.")