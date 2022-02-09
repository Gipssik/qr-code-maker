import datetime

from sqlalchemy import Column, DateTime, String

from database import Base


class QRCode(Base):
    __tablename__ = 'qrcodes'

    id = Column(String(64), primary_key=True, index=True)
    delete_hash = Column(String(255), nullable=False, unique=True)
    link = Column(String(512), nullable=False, unique=True)
    content = Column(String(512), nullable=False)
    date_created = Column(DateTime, nullable=False, default=datetime.datetime.now)

