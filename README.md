# ⚡ Thermal Grid Simulator

A cloud-inspired backend system that simulates IoT-controlled thermal devices and processes real-time data using a decoupled, queue-based architecture.

---

## 🚀 Overview

This project models how smart energy systems (e.g., water heaters, heat pumps) can act as grid-responsive devices by sending telemetry data to a backend system.

The system is designed to reflect **real-world distributed architectures**, focusing on scalability, reliability, and clean separation of concerns.

---

## 🧠 Architecture

```
Simulator → API → Redis Queue → Worker → PostgreSQL
```

### Components

* **Simulator**

  * Generates realistic IoT device data (temperature, energy usage, timestamp)
  * Sends HTTP requests to the API

* **API (FastAPI)**

  * Receives and validates incoming data
  * Pushes messages to Redis queue (no direct DB writes)

* **Queue (Redis)**

  * Buffers incoming data
  * Decouples ingestion from processing

* **Worker**

  * Consumes messages from Redis
  * Processes and stores data in the database

* **Database (PostgreSQL)**

  * Stores device telemetry data persistently

---

## 🎯 What This Project Demonstrates

* Designing **decoupled backend systems**
* Handling **real-time data ingestion pipelines**
* Implementing **queue-based architectures**
* Writing **clean, modular, production-style python3 code**
* Managing infrastructure via environment configuration

---

## 🧱 Tech Stack

* python3
* FastAPI
* Redis
* PostgreSQL
* SQLAlchemy
* Pydantic

---

## ▶️ How to Run


### 0. Configure Environment Variables
Create a .env file in the project root:

* DB_USER=your_user 
* DB_PASSWORD=your_password
* DB_HOST=localhost
* DB_PORT=5432
* DB_NAME=thermal_db

* REDIS_HOST=localhost
* REDIS_PORT=6379

Adjust values based on your local setup.

### 1. Install dependencies

```bash
python3 -m pip install -e .
```

---

### 2. Start Redis


Make sure you have Docker installed.
```bash
docker run -d \
  -p ${REDIS_PORT:-6379}:6379 \
  --name redis-local \
  redis
```
Notes:
Uses default port 6379 if REDIS_PORT is not set

If container already exists:
```bash
docker start redis-local
```

---

### 3. Run API

```bash
uvicorn thermal_grid_simulator.app.main:app --reload
```

---

### 4. Run Worker

```bash
python3 -m thermal_grid_simulator.worker.worker
```

---

### 5. Run Simulator

```bash
python3 -m thermal_grid_simulator.simulator.device_simulator
```

---

## 📊 Example Data

```json
{
  "device_id": 1,
  "temperature": 55.2,
  "energy_usage": 1.8,
  "timestamp": "2026-04-25T10:30:00Z"
}
```

---

## 👤 Author

Shapagat Bolat

---
