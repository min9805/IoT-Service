import datetime

from pydantic import BaseModel


# 요청 본문을 위한 Pydantic 모델

class Device(BaseModel):
    uuid: str
    registe_date: datetime.datetime


class DeviceRegister(BaseModel):
    create_date: datetime.datetime
    modify_date: datetime.datetime


class DeviceRegist(BaseModel):
    uuid: str
