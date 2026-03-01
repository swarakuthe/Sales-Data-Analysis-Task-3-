import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

# Clean data
print(df.isnull().sum())

df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(df['Price'].mean())

df = df.drop_duplicates()

print(df.isnull().sum())
print("Shape after cleaning:", df.shape)

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['Price']

# Analysis

total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)

total_quantity = df['Quantity'].sum()
print("Total Quantity Sold:", total_quantity)

best_product_quantity = df.groupby('Product')['Quantity'].sum()
print("Best Product by Quantity:", best_product_quantity.idxmax())

best_product_revenue = df.groupby('Product')['Revenue'].sum()
print("Best Product by Revenue:", best_product_revenue.idxmax())

top3_products = best_product_revenue.sort_values(ascending=False).head(3)
print("Top 3 Products by Revenue:")
print(top3_products)

highest_sale = df['Revenue'].max()
print("Highest Single Sale:", highest_sale)

lowest_sale = df['Revenue'].min()
print("Lowest Single Sale:", lowest_sale)

unique_products = df['Product'].nunique()
print("Total Unique Products:", unique_products)

average_revenue = best_product_revenue.mean()
print("Average Revenue per Product:", average_revenue)
