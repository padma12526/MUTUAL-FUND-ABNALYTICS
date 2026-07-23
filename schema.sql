CREATE DATABASE MutualFundDB;
GO

USE MutualFundDB;
GO

CREATE TABLE benchmark_indices (
    date VARCHAR(60),
    index_name VARCHAR(60),
    close_value DECIMAL(18,2)
);

CREATE TABLE investor_transaction_import (
    investor_id VARCHAR(60),
    transaction_date VARCHAR(60),
    amfi_code INT,
    transaction_type VARCHAR(60),
    amount_inr INT,
    state VARCHAR(60),
    city VARCHAR(60),
    city_tier VARCHAR(60),
    age_group VARCHAR(60),
    gender VARCHAR(60),
    annual_income_lakh DECIMAL(18,2),
    payment_mode VARCHAR(60),
    kyc_status VARCHAR(60)
);

CREATE TABLE scheme_performance_import (
    ...
);

CREATE TABLE nav_history_import (
    ...
);

CREATE TABLE aum_by_fund_house_import (
    ...
);

-- Continue until every table is included.