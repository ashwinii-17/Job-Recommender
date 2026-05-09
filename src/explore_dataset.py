import pandas as pd

# Load dataset
df = pd.read_csv("data/all_job_post.csv")

# Show first rows
print("🔹 First 5 rows:")
print(df.head())

# Show columns
print("\n🔹 Columns:")
print(df.columns)

# Show basic info
print("\n🔹 Info:")
print(df.info())
