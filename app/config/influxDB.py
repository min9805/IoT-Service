import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from starlette.config import Config


config = Config('.env')

token = config.get("INFLUXDB_TOKEN")
org = config.get("INFLUXDB_ORG")
url = config.get("INFLUXDB_URL")

influx_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
