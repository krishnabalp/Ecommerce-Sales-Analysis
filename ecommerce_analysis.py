import pandas as pd
file_path =r"D:\study\Data Science\Project\ecommerce_dataset.xlsx"
df = pd.read_excel(file_path)
print(df.head())

print("Shape:", df.shape)
print("Columns:", df.columns)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())


df = df.drop_duplicates()
df['Category'] = df['Category'].fillna("Unknown")
df['Payment_Method'] = df['Payment_Method'].fillna("Not Specified")
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
df = df.dropna(subset=['Purchase_Date'])
df['Discount_Amount'] = df['Price (Rs.)'] - df['Final_Price(Rs.)']
df['Purchase_Month'] = df['Purchase_Date'].dt.month_name()
print(df.head())

total_sales = df['Final_Price(Rs.)'].sum()
print("Total Sales:", total_sales)

orders_per_category = df['Category'].value_counts()
print(orders_per_category)

sales_per_category = df.groupby('Category')['Final_Price(Rs.)'].sum()
print(sales_per_category)

sales_per_month = df.groupby('Purchase_Month')['Final_Price(Rs.)'].sum()
print(sales_per_month)

df.to_csv("cleaned_ecommerce_data.csv", index=False)
print("File saved successfully")


