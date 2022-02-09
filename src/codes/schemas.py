import datetime

from pydantic import BaseModel


class QRCodeBase(BaseModel):
    content: str


class QRCodeCreate(QRCodeBase):
    pass


class QRCode(QRCodeBase):
    id: str
    delete_hash: str
    link: str
    date_created: datetime.datetime

    class Config:
        orm_mode = True
