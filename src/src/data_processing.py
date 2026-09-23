import os
import zipfile
import urllib.request

# NASA CMAPSS dataset URL
url = "https://data.nasa.gov/docs/legacy/CMAPSSData.zip"

# File names
zip_file = "CMAPSSData.zip"
data_folder = "CMAPSSData"

# Download dataset if it doesn't exist
if not os.path.exists(zip_file):
    print("Downloading NASA CMAPSS dataset...")
    urllib.request.urlretrieve(url, zip_file)
    print("Download completed.")

# Extract dataset if folder doesn't exist
if not os.path.exists(data_folder):
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(data_folder)
    print("Extraction completed.")

# Check extracted files
print("\nDataset files:")
for root, dirs, files in os.walk(data_folder):
    for file in files:
        print(os.path.join(root, file))
