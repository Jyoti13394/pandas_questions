import pandas as pd

df = pd.read_csv('Orders.csv')

print(df)

# Get max sales

print(df.sales.max())

# Select category wise count, max and min sales

print(df.groupby('category').sales.agg(['count', 'min', 'max']))

# Select city wise avg(sales), max(profit)

print(df.groupby('city').agg({'profit': max, 'sales':min}))
