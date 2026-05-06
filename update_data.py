import os
import urllib.request
import subprocess

def download_latest_data():
    url = "https://ir.eia.gov/wpsr/table1.csv"
    output_path = "table1.csv"
    
    print(f"Downloading latest WPSR data from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(output_path, 'wb') as f:
                f.write(response.read())
        print(f"Successfully downloaded {output_path}")
    except Exception as e:
        print(f"Error downloading data: {e}")
        return False
    return True

def run_pipeline():
    print("Running process_oil_data.py...")
    try:
        subprocess.run(["python", "process_oil_data.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running process_oil_data.py: {e}")
        return False

    print("Running build_dashboard.py...")
    try:
        subprocess.run(["python", "build_dashboard.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running build_dashboard.py: {e}")
        return False
        
    return True

if __name__ == "__main__":
    # Ensure we are in the correct directory (where this script is located)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    if download_latest_data():
        if run_pipeline():
            print("Pipeline completed successfully!")
        else:
            print("Pipeline failed during processing/building.")
    else:
        print("Pipeline failed during download.")
