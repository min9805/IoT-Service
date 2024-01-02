from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from app.domain.user import user_router
from app.models.device import Device
from app.db.database import create_tables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)

# create_tables()

load_dotenv()

token = os.getenv("INFLUXDB_TOKEN")
org = "yido"
url = "http://localhost:8086"
bucket="botanic"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

@app.get("/write")
def write_db():
    write_api = write_client.write_api(write_options=SYNCHRONOUS)


    point = (
    Point("measurement1")
    .tag("test_name", "uuid_example")
    .field("soil_humidity", 37.2)
    )
    write_api.write(bucket=bucket, org="yido", record=point)

    return {"status" : "success"}

@app.get("/write_uuid")
def write_db():
    write_api = write_client.write_api(write_options=SYNCHRONOUS)


    point = (
    Point("measurement1")
    .tag("user_id", "test_user_id")
    .tag("uuid", "test_uuid")
    .field("soil_humidity", 38.2)
    )
    write_api.write(bucket=bucket, org="yido", record=point)

    return {"status" : "success"}

@app.get("/read")
def write_db():
    query_api = write_client.query_api()

    query = """from(bucket: "botanic")
      |> range(start: -10m)
      |> filter(fn: (r) => r._measurement == "measurement1")
      |> filter(fn: (r) => r.test_name == "uuid_example")
      """
    tables = query_api.query(query, org="yido")

    return tables


@app.post("/read_post")
def write_db(device: Device):
    query_api = write_client.query_api()

    # 쿼리에 device.user_id 와 device.uuid 사용
    query = f"""
    from(bucket: "botanic")
      |> range(start: -10m)
      |> filter(fn: (r) => r._measurement == "measurement1")
      |> filter(fn: (r) => r.user_id == "{device.user_id}")
      |> filter(fn: (r) => r.uuid == "{device.uuid}")
    """
    tables = query_api.query(query, org="yido")

    return tables
