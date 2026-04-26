from fastapi.testclient import TestClient
from thermal_grid_simulator.app.main import app

client = TestClient(app)

def test_ingest_endpoint():
    payload = {
        "device_id": 1,
        "temperature": 50,
        "energy_usage": 1.5,
        "outside_temp": 10,
        "price_signal": "low",
        "timestamp": "2026-04-26T10:00:00+00:00"
    }

    response = client.post("/ingest-data", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "success"