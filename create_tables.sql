CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

CREATE TABLE regions(
  region_id INT PRIMARY KEY,
  region_name VARCHAR(50)
);

CREATE TABLE products(
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100),
  category VARCHAR(50),
  unit_price DECIMAL(10,2)
);

CREATE TABLE sales(
  sale_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT,
  region_id INT,
  sale_date DATE,
  quantity INT,
  discount DECIMAL(5,2),
  total_amount DECIMAL(10,2),
  FOREIGN KEY(product_id) REFERENCES products(product_id),
  FOREIGN KEY(region_id) REFERENCES regions(region_id)
);