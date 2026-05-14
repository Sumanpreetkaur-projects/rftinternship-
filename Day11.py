import matplotlib.pyplot as plt

# Dataset from project 37308.jpg
dates = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(dates, sales, marker='o', linestyle='-', color='b', label='Daily Sales')

# Bonus: Add Labels & Title
plt.title('Weekly Sales Trend Analysis')
plt.xlabel('Days of the Week')
plt.ylabel('Sales Units')

# Bonus: Highlight Highest and Lowest Day
high_val = max(sales)
low_val = min(sales)

high_day = dates[sales.index(high_val)]
low_day = dates[sales.index(low_val)]

plt.annotate(f'Highest: {high_val}', xy=(high_day, high_val), xytext=(high_day, high_val+10),
             arrowprops=dict(facecolor='green', shrink=0.05), ha='center')

plt.annotate(f'Lowest: {low_val}', xy=(low_day, low_val), xytext=(low_day, low_val-20),
             arrowprops=dict(facecolor='red', shrink=0.05), ha='center')

# Focus: Trend Analysis
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show the result
plt.tight_layout()
plt.show()
