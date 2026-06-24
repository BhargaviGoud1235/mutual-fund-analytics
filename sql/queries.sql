
-- 1. Top NAV funds
SELECT amfi_code, MAX(date), nav FROM fact_nav GROUP BY amfi_code ORDER BY nav DESC LIMIT 5;

-- 2. Average NAV
SELECT amfi_code, AVG(nav) FROM fact_nav GROUP BY amfi_code ORDER BY AVG(nav) DESC LIMIT 5;

-- 3. Transaction counts
SELECT transaction_type, COUNT(*) FROM fact_transactions GROUP BY transaction_type;

-- 4. State investment
SELECT state, SUM(amount_inr) FROM fact_transactions GROUP BY state ORDER BY SUM(amount_inr) DESC LIMIT 5;

-- 5. SIP vs Lumpsum
SELECT transaction_type, SUM(amount_inr) FROM fact_transactions GROUP BY transaction_type;

-- 6. Active funds
SELECT amfi_code, COUNT(*) FROM fact_nav GROUP BY amfi_code ORDER BY COUNT(*) DESC LIMIT 5;

-- 7. SIP trend
SELECT strftime('%Y-%m', transaction_date), SUM(amount_inr) FROM fact_transactions WHERE transaction_type='Sip' GROUP BY 1;

-- 8. Avg transaction amount
SELECT transaction_type, AVG(amount_inr) FROM fact_transactions GROUP BY transaction_type;

-- 9. City investment
SELECT city, SUM(amount_inr) FROM fact_transactions GROUP BY city ORDER BY SUM(amount_inr) DESC LIMIT 5;

-- 10. Top investors
SELECT investor_id, SUM(amount_inr) FROM fact_transactions GROUP BY investor_id ORDER BY SUM(amount_inr) DESC LIMIT 5;
