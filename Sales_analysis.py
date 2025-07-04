import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('diff_orders.csv')

df['Time'] = pd.to_datetime(df['Transaction Date'])
df['Hour'] = df['Time'].dt.hour

products = ['Coffee', 'Tea', 'Juice']

plt.figure(figsize=(10, 5))
for product in products:
          product_df = df[df['Product Name'] == product]
          hourly_counts = product_df['Hour'].value_counts().sort_index()
          hourly_counts = hourly_counts.reindex(range(24), fill_value=0)
          plt.plot(hourly_counts.index,
                   hourly_counts.values,
                   label=product,
                   marker='o')

plt.title('Hourly Sales per Product (Coffee, Tea, Juice)', fontsize=25)
plt.xlabel('Hour of the Day (0–23)', fontsize=16)
plt.ylabel('Number of Purchases', fontsize=16)
plt.xticks(range(24))
plt.grid(True)
plt.legend(title="Product", fontsize=14)
plt.show()
