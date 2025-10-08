import pandas as pd, random
from faker import Faker
from datetime import date

fake = Faker()
products = pd.read_csv("../data/products.csv")
regions = pd.read_csv("../data/regions.csv")

rows=[]
for i in range(1,5001):
    p=random.choice(products.itertuples())
    r=random.choice(regions.itertuples())
    qty=random.randint(1,50)
    disc=round(random.choice([0,0.05,0.1,0.15]),2)
    total=p.unit_price*qty*(1-disc)
    random_date=fake.date_between_dates(date_start=date(2023,1,1),date_end=date(2025,1,1))
    rows.append([i,p.product_id,r.region_id,random_date,qty,disc,total])
df=pd.DataFrame(rows,columns=["sale_id","product_id","region_id","sale_date","quantity","discount","total_amount"])
df.to_csv("../data/sales_data.csv",index=False)
print("5000-row dataset generated.")
