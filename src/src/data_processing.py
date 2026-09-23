import os
import zipfile
import subprocess

zip_file = "CMAPSSData.zip"
data_folder = "CMAPSSData"

url = "https://data.nasa.gov/docs/legacy/CMAPSSData.zip"

# Download dataset using wget
if not os.path.exists(zip_file):
    print("Downloading NASA CMAPSS dataset...")
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

# Show extracted files
print("\nDataset files:")
for root, dirs, files in os.walk(data_folder):
    for file in files:
        print(os.path.join(root, file))
