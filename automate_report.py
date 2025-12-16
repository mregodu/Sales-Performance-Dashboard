import pandas as pd, sqlalchemy
from datetime import datetime
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sales_db')

queries = {
  "Monthly_Sales":"SELECT DATE_FORMAT(sale_date,'%Y-%m') AS Month,SUM(total_amount) AS Total_Sales FROM sales GROUP BY Month;",
  "Top_Products":"SELECT p.product_name,SUM(s.total_amount) AS Revenue FROM sales s JOIN products p ON s.product_id=p.product_id GROUP BY p.product_name ORDER BY Revenue DESC LIMIT 10;",
  "Regional_Sales":"SELECT r.region_name,SUM(s.total_amount) AS Regional_Sales FROM sales s JOIN regions r ON s.region_id=r.region_id GROUP BY r.region_name;"
}

for name,q in queries.items():
    df=pd.read_sql(q,engine)
    file_name=f"../data/{name}_{datetime.now():%Y_%m_%d}.csv"
    df.to_csv(file_name,index=False)
print("Reports exported successfully.")
