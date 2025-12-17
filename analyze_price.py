import pandas as pd
import matplotlib.pyplot as plt

# 1. Prepare Data (Real market data scraped previously)
# Simulated data source: 18 competitor prices
raw_data = [
    '$25', '$195', '$10', '$40', '$125', '$35', 
    '$30', '$225', '$95', '$150', '$20', '$50',
    '$15', '$30', '$25', '$45', '$60', '$180'
]

print(f"📦 Raw Data: {raw_data}")

# 2. Data Cleaning
# The machine cannot read the '$' symbol, so we convert it to integers.
clean_prices = []
for price in raw_data:
    # Remove '$' symbol, strip whitespace, and convert to int
    num = int(price.replace('$', '').strip())
    clean_prices.append(num)

# Create a DataFrame using Pandas
df = pd.DataFrame(clean_prices, columns=['Price'])

# 3. Calculate Key Metrics
avg_price = df['Price'].mean()       # Average Price
median_price = df['Price'].median()  # Median Price (Less affected by outliers)
min_price = df['Price'].min()        # Minimum Price (The "Lowballers")
max_price = df['Price'].max()        # Maximum Price (The "Premium")

print("\n" + "="*30)
print("📊 Market Intelligence Report")
print("="*30)
print(f"💰 Average Price: ${avg_price:.2f}")
print(f"⚖️ Median Price:  ${median_price:.2f} <--- Recommended Starting Point")
print(f"📉 Min Price:     ${min_price}")
print(f"📈 Max Price:     ${max_price}")

# 4. Data Visualization
plt.figure(figsize=(10, 6))

# Plot Histogram - visualize price distribution
# color='#1dbf73' is the Fiverr Brand Green
plt.hist(df['Price'], bins=8, color='#1dbf73', edgecolor='black', alpha=0.7)

# Add a red dashed line for Average Price
plt.axvline(avg_price, color='red', linestyle='dashed', linewidth=2, label=f'Avg: ${avg_price:.0f}')

# Add a blue dashed line for Median Price
plt.axvline(median_price, color='blue', linestyle='dashed', linewidth=2, label=f'Median: ${median_price:.0f}')

# Set Titles and Labels
plt.title('Fiverr PCB Design Service Price Distribution', fontsize=14)
plt.xlabel('Price ($)', fontsize=12)
plt.ylabel('Number of Sellers (Count)', fontsize=12)
plt.legend()  # Show legend
plt.grid(axis='y', alpha=0.3) # Add light grid lines for readability

# 5. Display Plot
print("\n🖼️ Generating Chart...")
plt.show()