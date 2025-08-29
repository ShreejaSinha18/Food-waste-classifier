import os
import subprocess

DATA_DIR = "data"
DATASET_PATH = os.path.join(DATA_DIR, "dataset.zip")
HYPERAI_URL = os.environ.get("HYPERAI_URL", "https://orion.hyper.ai/tracker/download?torrent=32450")

def download_dataset():
    os.makedirs(DATA_DIR, exist_ok=True)

    print(f"📥 Downloading dataset from {HYPERAI_URL} ...")

    # Use aria2c to handle torrent/HTTP automatically
    try:
        subprocess.run([
            "aria2c",
            "-d", DATA_DIR,
            "-o", "dataset.zip",
            HYPERAI_URL
        ], check=True)
    except FileNotFoundError:
        print("❌ aria2c not found. Please install it with:")
        print("   sudo apt-get update && sudo apt-get install -y aria2")
        return
    except subprocess.CalledProcessError:
        print("❌ Download failed. Check the URL or internet connection.")
        return

    if os.path.exists(DATASET_PATH):
        print(f"✅ Dataset downloaded and saved to {DATASET_PATH}")
    else:
        print("❌ Dataset download failed: file not found.")

if __name__ == "__main__":
    download_dataset()
