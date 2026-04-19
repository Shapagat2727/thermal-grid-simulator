from fastapi import FastAPI
import logging
from fastapi import Depends
from sqlalchemy.orm import Session
from thermal_grid_simulator.app.database import engine
from thermal_grid_simulator.app import models
from thermal_grid_simulator.app.database import SessionLocal
from thermal_grid_simulator.app.models import DeviceData
from thermal_grid_simulator.app.schemas import DeviceDataCreate

logging.basicConfig(level=logging.INFO)
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Basic health check endpoint
@app.get("/")
def root():
    return {"message": "Thermal Grid API running"}

# Endpoint to ingest data from devices
@app.post("/ingest-data")
def ingest_data(data: DeviceDataCreate, db: Session = Depends(get_db)):
    db_data = DeviceData(
        device_id=data.device_id,
        temperature=data.temperature,
        energy_usage=data.energy_usage
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return {"status": "success", "id": db_data.id}

# Endpoint to retrieve recent device data
@app.get("/devices")
def get_data(db: Session = Depends(get_db)):
    logging.info(f"Received data from device {DeviceData.device_id}")
    return db.query(DeviceData).limit(50).all()
