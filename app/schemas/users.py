from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    create_time: datetime
    update_time: datetime
    deleted: bool
    hashed_password: str
    disabled: bool

    class Config:
        orm_mode = True
