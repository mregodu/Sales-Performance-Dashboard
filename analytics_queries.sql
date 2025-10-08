-- Monthly Sales Trend
SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(total_amount) AS total_sales
FROM sales GROUP BY month ORDER BY month;

-- Top 10 Products
SELECT p.product_name, SUM(s.total_amount) AS revenue
FROM sales s JOIN products p ON s.product_id=p.product_id
GROUP BY p.product_name ORDER BY revenue DESC LIMIT 10;

-- Regional Performance
SELECT r.region_name, SUM(s.total_amount) AS total_sales
FROM sales s JOIN regions r ON s.region_id=r.region_id
GROUP BY r.region_name ORDER BY total_sales DESC;

-- Discount Effectiveness
SELECT p.category, ROUND(AVG(s.discount)*100,2) AS avg_discount,
       SUM(s.total_amount) AS revenue
FROM sales s JOIN products p ON s.product_id=p.product_id
GROUP BY p.category;
