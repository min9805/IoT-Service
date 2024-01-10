from datetime import datetime

from sqlalchemy.orm import Session

from app.config.models import Question, Answer, User, Device
from app.domain.device.device_schema import DeviceRegist


def registe_device(db: Session, device_regist: DeviceRegist, db_user: User):
    db_device = Device(uuid=device_regist.uuid,
                       regist_date=datetime.now(),
                       user=db_user)
    db.add(db_device)
    db.commit()


def get_device_list(db: Session, db_user: User, skip: int = 0, limit: int = 10, keyword: str = ''):
    user_devices = db.query(Device).filter(Device.user_id == db_user.id).all()
    print(db_user.id)
    return 1, user_devices
