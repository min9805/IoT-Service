from pydantic import BaseModel

# 요청 본문을 위한 Pydantic 모델
class Device(BaseModel):
    user_id: str
    uuid: str

