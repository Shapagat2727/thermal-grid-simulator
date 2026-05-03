from thermal_grid_simulator.simulator.device_simulator import generate_energy_usage

def test_energy_increases_when_cold(monkeypatch):
    def mock_temp():
        return 0  # very cold

    monkeypatch.setattr(
        "thermal_grid_simulator.simulator.device_simulator.get_current_temperature",
        mock_temp
    )

    usage = generate_energy_usage()
    assert usage > 0.5


def test_energy_low_when_warm(monkeypatch):
    def mock_temp():
        return 25  # warm

    monkeypatch.setattr(
        "thermal_grid_simulator.simulator.device_simulator.get_current_temperature",
        mock_temp
    )

    usage = generate_energy_usage()
    assert usage == 0.5