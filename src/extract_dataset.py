import zipfile
import os

# Paths
zip_path = "data/dataset.zip"
extract_dir = "data/"

def extract_dataset():
    if not os.path.exists(zip_path):
        print("❌ Dataset zip file not found. Please download it first.")
        return
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        print(f"✅ Dataset extracted to {extract_dir}")

if __name__ == "__main__":
    extract_dataset()
