
-- Total Revenue
SELECT SUM(total_revenue) AS total_revenue FROM data;

-- Total Profit
SELECT SUM(total_revenue - total_unit_cost) AS total_profit FROM data;

-- Top 10 Customers by Revenue
SELECT customer_name, SUM(total_revenue) AS revenue
FROM data
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 10;

-- Monthly Sales Trend
SELECT MONTH(orderdate) AS month, SUM(total_revenue) AS revenue
FROM data
GROUP BY month
ORDER BY month;

-- Region-wise Sales
SELECT region, SUM(total_revenue) AS revenue
FROM data
GROUP BY region
ORDER BY revenue DESC;

-- Average Order Value
SELECT AVG(total_revenue) AS avg_order_value FROM data;
