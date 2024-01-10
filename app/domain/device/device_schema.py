import datetime

from pydantic import BaseModel

from app.domain.user.user_schema import User


# 요청 본문을 위한 Pydantic 모델

class Device(BaseModel):
    uuid: str
    regist_date: datetime.datetime
    user: User
    device_name: str

    class Config:
        orm_mode = True


class DeviceRegister(BaseModel):
    create_date: datetime.datetime
    modify_date: datetime.datetime


class DeviceRegist(BaseModel):
    uuid: str


class DeviceList(BaseModel):
    total: int = 0
    device_list: list[Device] = []

class WriteDeviceData(BaseModel):
    uuid: str
    value: float