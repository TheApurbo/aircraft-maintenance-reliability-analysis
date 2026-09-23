import os
import zipfile
import subprocess
import pandas as pd

zip_file = "CMAPSSData.zip"
data_folder = "CMAPSSData"

url = "https://zenodo.org/records/15346912/files/CMAPSSData.zip?download=1"

# Download dataset
if not os.path.exists(zip_file):
    print("Downloading NASA C-MAPSS dataset...")
    subprocess.run(
        ["wget", "-O", zip_file, url],
        check=True
    )
    print("Download completed.")

# Extract dataset
if not os.path.exists(data_folder):
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(data_folder)
    print("Extraction completed.")

# Find FD001 training file
train_file = None

for root, dirs, files in os.walk(data_folder):
    if "train_FD001.txt" in files:
        train_file = os.path.join(root, "train_FD001.txt")
        break

if train_file is None:
    raise FileNotFoundError("train_FD001.txt not found!")

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
print("Training file:", train_file)
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFirst 5 rows:")
print(df.head())

print("\nRUL statistics:")
print(df["RUL"].describe())
# Basic data analysis
print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nNumber of engines:")
print(df["unit_id"].nunique())

print("\nAverage RUL:")
print(df["RUL"].mean())

print("\nRUL by engine:")
print(
    df.groupby("unit_id")["RUL"]
    .agg(["min", "max", "mean"])
    .head(10)
)
import matplotlib.pyplot as plt

# Plot RUL degradation for first 5 engines
plt.figure(figsize=(10, 6))

for engine_id in df["unit_id"].unique()[:5]:
    engine_data = df[df["unit_id"] == engine_id]
    plt.plot(
        engine_data["cycle"],
        engine_data["RUL"],
        label=f"Engine {engine_id}"
    )

plt.xlabel("Operating Cycle")
plt.ylabel("Remaining Useful Life (RUL)")
plt.title("Engine Degradation and Remaining Useful Life")
plt.legend()
plt.grid(True)

os.makedirs("outputs", exist_ok=True)

plt.savefig(
    "outputs/rul_degradation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nRUL degradation graph saved successfully!")
