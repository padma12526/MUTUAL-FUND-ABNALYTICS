-- ==========================================
-- Mutual Fund Analytics - queries.sql
-- ==========================================

-- 1. Total number of schemes
SELECT COUNT(*) AS total_schemes
FROM scheme_performance_import;

-- 2. Top 10 schemes by 5-year return
SELECT TOP 10
    scheme_name,
    fund_house,
    return_5_year_pct
FROM scheme_performance_import
ORDER BY return_5_year_pct DESC;

-- 3. Average expense ratio by category
SELECT
    category,
    AVG(expense_ratio) AS avg_expense_ratio
FROM scheme_performance_import
GROUP BY category
ORDER BY avg_expense_ratio DESC;

-- 4. Top 10 fund houses by AUM
SELECT TOP 10
    fund_house,
    SUM(aum_crore) AS total_aum
FROM scheme_performance_import
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 5. Number of investors by state
SELECT
    state,
    COUNT(*) AS total_investors
FROM investor_transaction_import
GROUP BY state
ORDER BY total_investors DESC;

-- 6. Total transaction amount by transaction type
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM investor_transaction_import
GROUP BY transaction_type
ORDER BY total_amount DESC;

-- 7. Benchmark closing values
SELECT
    index_name,
    AVG(close_value) AS average_close_value
FROM benchmark_indices
GROUP BY index_name;

-- 8. Monthly SIP inflows
SELECT
    month,
    sip_inflow_crore
FROM monthly_sip_inflows_import
ORDER BY month;

-- 9. Category-wise net inflows
SELECT
    category,
    SUM(net_inflow_crore) AS total_net_inflow
FROM category_inflows_import
GROUP BY category
ORDER BY total_net_inflow DESC;

-- 10. Average alpha and beta by category
SELECT
    category,
    AVG(alpha) AS average_alpha,
    AVG(beta) AS average_beta
FROM scheme_performance_import
GROUP BY category;