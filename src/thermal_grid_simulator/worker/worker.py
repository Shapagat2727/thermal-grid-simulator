from thermal_grid_simulator.app.redis_client import redis_client
from thermal_grid_simulator.app.database import SessionLocal
from thermal_grid_simulator.app.models import DeviceData

import json

def process_message(data):
    db = SessionLocal()

    db_data = DeviceData(
        device_id=data["device_id"],
        temperature=data["temperature"],
        energy_usage=data["energy_usage"],
        timestamp=data["timestamp"]
    )

    db.add(db_data)
    db.commit()
    db.close()

while True:
    message = redis_client.brpop("device_queue")
    data = json.loads(message[1])
    

    print("Processing:", data)
    process_message(data)
