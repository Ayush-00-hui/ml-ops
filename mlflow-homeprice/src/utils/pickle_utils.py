import os
import pandas as pd

base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "raw")
csv_path = os.path.join(base_dir, "house_prices.csv")
pkl_path = os.path.join(base_dir, "house_prices.pkl")

# Read CSV file
df = pd.read_csv(csv_path)

# Save DataFrame as a pickle file
df.to_pickle(pkl_path)

print("DataFrame saved as pickle.")

# load pickle
df = pd.read_pickle(pkl_path)

print(df.head())
