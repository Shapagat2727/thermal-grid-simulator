import json
import logging
import time
from thermal_grid_simulator.app.redis_client import redis_client
from thermal_grid_simulator.app.database import SessionLocal
from thermal_grid_simulator.app.models import DeviceData

logging.basicConfig(level=logging.INFO)

MAX_RETRIES = 3


def process_message(data):
    db_data = build_device_data(data)
    save_to_db(db_data)


def build_device_data(data):
    return DeviceData(
        device_id=data["device_id"],
        temperature=data["temperature"],
        energy_usage=data["energy_usage"],
        timestamp=data["timestamp"]
    )

def save_to_db(db_data):
    db = SessionLocal()
    db.add(db_data)
    db.commit()
    db.close()


def run_worker():
    while True:
        message = redis_client.brpop("device_queue")
        raw_data = message[1]
        data = json.loads(raw_data)

        retries = data.get("retries", 0)

        try:
            logging.info(f"Processing device {data['device_id']}")
            process_message(data)

        except Exception as e:
            logging.error(f"Error: {e}")

            if retries < MAX_RETRIES:
                time.sleep(1)
                data["retries"] = retries + 1
                redis_client.lpush("device_queue", json.dumps(data))
                logging.info(f"Retrying ({data['retries']})")

            else:
                redis_client.lpush("dead_letter_queue", json.dumps(data))
                logging.error("Moved to dead letter queue")

if __name__ == "__main__":
    run_worker()