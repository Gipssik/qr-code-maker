import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from codes.schemas import QRCode


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class User(UserBase):
    id: int
    date_created: datetime.datetime
    qrcodes: list[QRCode]

    class Config:
        orm_mode = True
