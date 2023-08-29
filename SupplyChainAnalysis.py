import pandas as pd
from sqlalchemy import *
import seaborn as sns
import matplotlib.pyplot as plt

# Define the database connection
DATABASE_URI = 'mysql://root:pppppppp@localhost/trial'  # Replace with your MySQL credentials and database name
engine = create_engine(DATABASE_URI, echo=True)

with engine.begin() as conn:
    query = text('SELECT * FROM supply_chain_data')
    data = pd.read_sql_query(query, conn)

# Load supply chain data from MySQL database
# query = "SELECT * FROM supply_chain_data"
# data = pd.read_sql(query, engine)

# Continue with the analysis calculations (same code as before)
average_transit_time = data.groupby('route')['transit_time'].mean()
print("Average Transit Time by Route:")
print(average_transit_time)
print("\n")

data['date'] = pd.to_datetime(data['date'])
inventory_over_time = data.groupby('date')['inventory'].sum()
print("Inventory Levels Over Time:")
print(inventory_over_time)
print("\n")

total_cost_by_route = data.groupby('route')['cost'].sum()
print("Cost Analysis by Route:")
print(total_cost_by_route)
print("\n")

transit_time_stats = data['transit_time'].describe()
print("Transit Time Distribution:")
print(transit_time_stats)
print("\n")

correlation = data['inventory'].corr(data['cost'])
print(f"Correlation between Inventory and Cost: {correlation:.2f}")

# Create visualizations
plt.figure(figsize=(10, 6))

# Visualization 1: Average Transit Time by Route
plt.subplot(2, 2, 1)
sns.barplot(x=average_transit_time.index, y=average_transit_time.values, color='skyblue')
plt.title('Average Transit Time by Route')

# Visualization 2: Inventory Levels Over Time
plt.subplot(2, 2, 2)
sns.lineplot(x=inventory_over_time.index, y=inventory_over_time.values, color='green')
plt.title('Inventory Levels Over Time')

# Visualization 3: Cost Analysis by Route
plt.subplot(2, 2, 3)
sns.barplot(x=total_cost_by_route.index, y=total_cost_by_route.values, color='orange')
plt.title('Cost Analysis by Route')
plt.xticks(rotation=45)

# Visualization 4: Transit Time Distribution
plt.subplot(2, 2, 4)
sns.histplot(data['transit_time'], bins=15, color='purple', alpha=0.7)
plt.title('Transit Time Distribution')

plt.tight_layout()
plt.show()
