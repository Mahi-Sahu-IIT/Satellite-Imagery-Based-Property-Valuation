import pandas as pd
import requests
import os
from time import sleep

# Load data
train = pd.read_excel(r"C:\Users\Mahi Sahu\OneDrive\Desktop\real_estate_multimodal\data\train.xlsx")

# Create folder if not exists
os.makedirs("images", exist_ok=True)

ACCESS_TOKEN = "sk.eyJ1IjoibWFoaXNhaHUiLCJhIjoiY21rM3dweGxjMDE3czNkczc0cjVkdG9idSJ9.Qp9PA2NpwiXm4XSeuCPOTg"
ZOOM = 16
WIDTH = 224
HEIGHT = 224
MAX_RETRIES = 3  # retry limit
SLEEP_BETWEEN_REQUESTS = 0.2  # seconds

def fetch_image(lat, lon, id):
    url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},{ZOOM}/{WIDTH}x{HEIGHT}?access_token={ACCESS_TOKEN}"
    for attempt in range(1, MAX_RETRIES+1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(f"images/{id}.png", "wb") as f:
                    f.write(response.content)
                print(f"Success for ID {id}")
                return
            else:
                print(f"Attempt {attempt}: Failed for ID {id}, status code {response.status_code}")
        except Exception as e:
            print(f"Attempt {attempt}: Exception for ID {id}: {e}")
        sleep(SLEEP_BETWEEN_REQUESTS)
    print(f"Failed after {MAX_RETRIES} attempts for ID {id}")

# Loop through dataset
for idx, row in train.iterrows():
    fetch_image(row['lat'], row['long'], row['id'])
    sleep(SLEEP_BETWEEN_REQUESTS)  # avoid hitting rate limits
