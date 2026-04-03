
import pandas as pd

# Load data
df = pd.read_excel('Custemers_Data.xlsx')

# 1. Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Handle missing values
df = df.dropna()

# 4. Convert date column
df['orderdate'] = pd.to_datetime(df['orderdate'])

# 5. Ensure numeric columns
df['total_unit_cost'] = pd.to_numeric(df['total_unit_cost'], errors='coerce')
df['total_revenue'] = pd.to_numeric(df['total_revenue'], errors='coerce')

# 6. Create new column: profit
df['profit'] = df['total_revenue'] - df['total_unit_cost']

# 7. Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

print(df.head())
