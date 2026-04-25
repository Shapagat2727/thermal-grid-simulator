from pydantic import BaseModel

class DeviceDataCreate(BaseModel):
    device_id: int
    temperature: float
    energy_usage: float
    timestamp: str