import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://127.0.0.1:8000/ingest-data"

def simulate_device(device_id):
    while True:
        data = {
            "device_id": device_id,
            "temperature": get_current_temperature(),
            "energy_usage": generate_energy_usage(),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

        try:
            response = requests.post(API_URL, json=data)
            print(f"Device {device_id}: {response.status_code}")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(random.uniform(1, 3))

def get_current_temperature():
    try:
        LATTITUDE = os.getenv("LATITUDE")
        LONGITUDE = os.getenv("LONGITUDE")
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={LATTITUDE}&longitude={LONGITUDE}&current=temperature_2m")
        if response.status_code == 200:
            data = response.json()
            return data['current']['temperature_2m']
    except Exception as e:
        print(f"Error fetching weather data: {e}")
    return None

def generate_energy_usage():
    '''
    Simulate energy usage based on temperature.
    For simplicity, we assume that energy usage increases as temperature decreases.
    '''
    temperature = get_current_temperature()
    base_usage = 0.5

    if temperature < 15:
        return base_usage + (15 - temperature) * 0.2

    return base_usage

if __name__ == "__main__":
    for i in range(5):  # simulate 5 devices
        import threading
        threading.Thread(target=simulate_device, args=(i,)).start()