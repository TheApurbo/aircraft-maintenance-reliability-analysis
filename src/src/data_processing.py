import os
import pandas as pd

data_folder = "CMAPSSData"

# NASA C-MAPSS FD001 dataset
train_file = os.path.join(data_folder, "train_FD001.txt")

# Column names
columns = [
    "unit_id", "cycle", "setting_1", "setting_2", "setting_3"
] + [f"sensor_{i}" for i in range(1, 22)]

# Load training data
df = pd.read_csv(
    train_file,
    sep=r"\s+",
    header=None,
    names=columns
)

# Calculate Remaining Useful Life (RUL)
max_cycle = df.groupby("unit_id")["cycle"].transform("max")
df["RUL"] = max_cycle - df["cycle"]

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFirst 5 rows:")
print(df.head())

print("\nRUL statistics:")
print(df["RUL"].describe())
