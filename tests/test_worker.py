from thermal_grid_simulator.worker.worker import build_device_data

def test_build_device_data():
    data = {
        "device_id": 1,
        "temperature": 50,
        "energy_usage": 1.5,
        "timestamp": "2026-04-26T10:00:00+00:00"
    }

    obj = build_device_data(data)

    assert obj.device_id == 1
    assert obj.temperature == 50
    assert obj.energy_usage == 1.5