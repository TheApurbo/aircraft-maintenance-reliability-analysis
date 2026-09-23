import os
import zipfile
import subprocess

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# ============================================================
# 1. Download and Extract NASA C-MAPSS Dataset
# ============================================================

zip_file = "CMAPSSData.zip"
data_folder = "CMAPSSData"

url = "https://zenodo.org/records/15346912/files/CMAPSSData.zip?download=1"

if not os.path.exists(zip_file):
    print("Downloading NASA C-MAPSS dataset...")

    subprocess.run(
        ["wget", "-O", zip_file, url],
        check=True
    )

    print("Download completed.")


if not os.path.exists(data_folder):
    print("Extracting dataset...")

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(data_folder)

    print("Extraction completed.")


# ============================================================
# 2. Find FD001 Training File
# ============================================================

train_file = None

for root, dirs, files in os.walk(data_folder):
    if "train_FD001.txt" in files:
        train_file = os.path.join(root, "train_FD001.txt")
        break

if train_file is None:
    raise FileNotFoundError("train_FD001.txt not found!")


# ============================================================
# 3. Load Dataset
# ============================================================

columns = [
    "unit_id",
    "cycle",
    "setting_1",
    "setting_2",
    "setting_3"
] + [f"sensor_{i}" for i in range(1, 22)]


df = pd.read_csv(
    train_file,
    sep=r"\s+",
    header=None,
    names=columns
)


# ============================================================
# 4. Calculate Remaining Useful Life (RUL)
# ============================================================

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


# ============================================================
# 5. Basic Data Analysis
# ============================================================

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


# ============================================================
# 6. Create Output Folder
# ============================================================

os.makedirs("outputs", exist_ok=True)


# ============================================================
# 7. RUL Degradation Visualization
# ============================================================

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

plt.savefig(
    "outputs/rul_degradation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nRUL degradation graph saved successfully!")


# ============================================================
# 8. Sensor Trend Analysis
# ============================================================

sensor_columns = [f"sensor_{i}" for i in range(1, 22)]

sensor_std = (
    df[sensor_columns]
    .std()
    .sort_values(ascending=False)
)

print("\nSensor variability:")
print(sensor_std)


top_sensors = sensor_std.head(5).index


plt.figure(figsize=(10, 6))

engine_1 = df[df["unit_id"] == 1]

for sensor in top_sensors:

    plt.plot(
        engine_1["cycle"],
        engine_1[sensor],
        label=sensor
    )

plt.xlabel("Operating Cycle")
plt.ylabel("Sensor Value")
plt.title("Top 5 Sensor Trends - Engine 1")
plt.legend()
plt.grid(True)

plt.savefig(
    "outputs/sensor_trends.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSensor trend graph saved successfully!")


# ============================================================
# 9. Machine Learning: RUL Prediction
# ============================================================

features = sensor_columns + [
    "setting_1",
    "setting_2",
    "setting_3"
]


# ============================================================
# 10. Engine-wise Train/Test Split
# ============================================================

# Use complete engines for either training or testing.
# This prevents measurements from the same engine
# appearing in both training and testing datasets.

unique_engines = df["unit_id"].unique()

rng = np.random.default_rng(42)

rng.shuffle(unique_engines)

split_index = int(len(unique_engines) * 0.8)

train_engines = unique_engines[:split_index]
test_engines = unique_engines[split_index:]


train_df = df[df["unit_id"].isin(train_engines)]
test_df = df[df["unit_id"].isin(test_engines)]


X_train = train_df[features]
y_train = train_df["RUL"]

X_test = test_df[features]
y_test = test_df["RUL"]


print("\nMachine Learning Dataset Split:")
print("Training engines:", len(train_engines))
print("Testing engines:", len(test_engines))
print("Training rows:", len(train_df))
print("Testing rows:", len(test_df))


# ============================================================
# 11. Train Random Forest Model
# ============================================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)


# ============================================================
# 12. Prediction
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 13. Model Evaluation
# ============================================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)


print("\nRUL Prediction Model Results:")
print("MAE:", mae)
print("RMSE:", rmse)


# ============================================================
# 14. Actual vs Predicted RUL
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.5
)

plt.xlabel("Actual RUL")
plt.ylabel("Predicted RUL")
plt.title("Actual vs Predicted Remaining Useful Life")


min_value = min(
    y_test.min(),
    y_pred.min()
)

max_value = max(
    y_test.max(),
    y_pred.max()
)


plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--"
)

plt.grid(True)

plt.savefig(
    "outputs/actual_vs_predicted_rul.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nActual vs Predicted RUL graph saved successfully!")
