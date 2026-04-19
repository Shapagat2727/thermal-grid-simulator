from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from thermal_grid_simulator.app.database import Base

class DeviceData(Base):
    __tablename__ = "device_data"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer)
    temperature = Column(Float)
    energy_usage = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)