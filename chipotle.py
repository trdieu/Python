import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Step 2: Import the dataset from the given address
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')

# Step 3: Assign it to a variable called chipo
# This step is already covered in the code above

# Step 4: See the first 10 entries
print(chipo.head(10))

# Step 5: Create a histogram of the top 5 items bought
item_counts = Counter(chipo['item_name'])
top_items = item_counts.most_common(5)

# Extract item names and their counts
items = [item[0] for item in top_items]
counts = [item[1] for item in top_items]

# Create the histogram
plt.figure(figsize=(10, 5))
plt.bar(items, counts, color='blue')
plt.xlabel('Items')
plt.ylabel('Number of Times Ordered')
plt.title('Top 5 Most Ordered Items at Chipotle')
plt.show()

# Step 6: Create a scatterplot with the number of items ordered per order price
# Remove the dollar sign and convert to float
chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype(float)

# Create the scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(chipo['item_price'], chipo['quantity'], alpha=0.5, color='green')
plt.xlabel('Order Price ($)')
plt.ylabel('Number of Items Ordered')
plt.title('Number of Items Ordered vs. Order Price')
plt.show()

# Step 7: BONUS: Create a question and a graph to answer your own question
# Question: What is the total revenue generated by each item?
# Calculate total revenue per item
chipo['total_revenue'] = chipo['quantity'] * chipo['item_price']
revenue_per_item = chipo.groupby('item_name').sum()['total_revenue']

# Sort and get the top 5 revenue generating items
top_revenue_items = revenue_per_item.sort_values(ascending=False).head(5)

# Plot the top 5 revenue generating items
plt.figure(figsize=(10, 5))
top_revenue_items.plot(kind='bar', color='orange')
plt.xlabel('Items')
plt.ylabel('Total Revenue ($)')
plt.title('Top 5 Revenue Generating Items at Chipotle')
plt.show()
