from datetime import datetime

from sqlalchemy.orm import Session

from app.config.models import Question, Answer, User, Device
from app.domain.device.device_schema import DeviceRegist


def registe_device(db: Session, device_regist: DeviceRegist, db_user: User):
    db_device = Device(uuid=device_regist.uuid,
                       regist_date=datetime.now(),
                       )
    db.add(db_device)
    db_user.device.append(db_device)
    db.commit()
