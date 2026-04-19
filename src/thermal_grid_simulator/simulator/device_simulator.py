import requests
import random
import time

API_URL = "http://127.0.0.1:8000/ingest-data"

def simulate_device(device_id):
    while True:
        data = {
            "device_id": device_id,
            "temperature": random.uniform(40, 70),
            "energy_usage": random.uniform(0.5, 3.0)
        }

        try:
            response = requests.post(API_URL, json=data)
            print(f"Device {device_id}: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    for i in range(5):  # simulate 5 devices
        import threading
        threading.Thread(target=simulate_device, args=(i,)).start()