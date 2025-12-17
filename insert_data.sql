USE sales_db;
LOAD DATA LOCAL INFILE 'data/regions.csv'
INTO TABLE regions
FIELDS TERMINATED BY ','
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'data/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ','
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'data/sales_data.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(sale_id, product_id, region_id, sale_date, quantity, discount, total_amount);
