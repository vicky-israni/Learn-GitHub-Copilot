import pandas as pd

# Load sales data from CSV
df = pd.read_csv('sales.csv')

# Filter rows where sales > 600
filtered_df = df[df['sales'] > 600]

print(filtered_df)