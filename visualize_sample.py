import pandas as pd, matplotlib.pyplot as plt
df=pd.read_csv("../data/sales_data.csv")
df['sale_date']=pd.to_datetime(df['sale_date'])
monthly=df.groupby(df['sale_date'].dt.to_period('M'))['total_amount'].sum()
monthly.plot(kind='line',title='Monthly Sales Trend',xlabel='Month',ylabel='Sales',figsize=(8,4))
plt.tight_layout(); plt.show()
