
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status
from starlette.config import Config

from app.config.database import get_db
from app.config.influxDB import influx_client as client
from app.domain.data.data_schema import Device

config = Config('.env')
ORG = config('INFLUXDB_ORG')
URL = config('INFLUXDB_URL')
BUCKET = config('INFLUXDB_BUCKET')

ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

router = APIRouter(
    prefix="/api/data",
)

@router.get("/write")
def write_db():
    write_api = client.write_api(write_options=SYNCHRONOUS)


    point = (
    Point("measurement1")
    .tag("test_name", "uuid_example")
    .field("soil_humidity", 37.2)
    )
    write_api.write(bucket=BUCKET, org=ORG, record=point)

    return {"status" : "success"}

@router.get("/write_uuid")
def write_db():
    write_api = client.write_api(write_options=SYNCHRONOUS)


    point = (
    Point("measurement1")
    .tag("user_id", "test_user_id")
    .tag("uuid", "test_uuid")
    .field("soil_humidity", 38.2)
    )
    write_api.write(bucket=BUCKET, org=ORG, record=point)

    return {"status" : "success"}

@router.get("/read")
def write_db():
    query_api = client.query_api()

    query = """from(bucket: "botanic")
      |> range(start: -24h)
      |> filter(fn: (r) => r._measurement == "measurement1")
      |> filter(fn: (r) => r.test_name == "uuid_example")
      """
    tables = query_api.query(query, org=ORG)

    return tables


@router.post("/read_post")
def write_db(device: Device):
    query_api = client.query_api()

    # 쿼리에 device.user_id 와 device.uuid 사용
    query = f"""
    from(bucket: "botanic")
      |> range(start: -24h)
      |> filter(fn: (r) => r._measurement == "measurement1")
      |> filter(fn: (r) => r.user_id == "{device.user_id}")
      |> filter(fn: (r) => r.uuid == "{device.uuid}")
    """
    tables = query_api.query(query, org=ORG)

    return tables
