import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the sales data
df = pd.read_csv('sales.csv')

# Plot histogram of sales grouped by category
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='sales', hue='category', multiple='stack', kde=False)
plt.title('Histogram of Sales Grouped by Category')
plt.xlabel('Sales')
plt.ylabel('Count')
plt.legend(title='Category')
plt.tight_layout()
plt.show()