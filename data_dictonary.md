# Mutual Fund Analytics - Data Dictionary

## Database
MutualFundDB

---

## Table: benchmark_indices

| Column | Data Type | Description |
|--------|-----------|-------------|
| date | VARCHAR(60) | Date of benchmark index |
| index_name | VARCHAR(60) | Name of the benchmark index |
| close_value | DECIMAL(18,2) | Closing value of the benchmark index |

---

## Table: investor_transaction_import

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | VARCHAR(60) | Unique investor identifier |
| transaction_date | VARCHAR(60) | Date of transaction |
| amfi_code | INT | AMFI scheme code |
| transaction_type | VARCHAR(60) | Purchase or redemption |
| amount_inr | INT | Transaction amount in INR |
| state | VARCHAR(60) | Investor state |
| city | VARCHAR(60) | Investor city |
| city_tier | VARCHAR(60) | Tier of the city |
| age_group | VARCHAR(60) | Investor age group |
| gender | VARCHAR(60) | Investor gender |
| annual_income_lakh | DECIMAL(18,2) | Annual income in lakh |
| payment_mode | VARCHAR(60) | Mode of payment |
| kyc_status | VARCHAR(60) | KYC verification status |

---

(Add the remaining tables in the same format.)