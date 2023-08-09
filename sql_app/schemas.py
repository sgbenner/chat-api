from datetime import datetime

from pydantic import BaseModel


class RoomBase(BaseModel):
    title: str
    description: str
    type: str
    creator: int
    settings: dict


class RoomCreate(RoomBase):
    pass


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


class Room(RoomBase):
    id: int
    create_time: datetime
    update_time: datetime
    deleted: bool
    users: list[User] = []

    class Config:
        orm_mode = True


## Notes:
# Anything in the _Create model will be required in the POST request
class RoomUserBase(BaseModel):
    room_id: int
    users: list[User]


class RoomUser(RoomUserBase):
    pass

    class Config:
        orm_mode = True


class RoomUserCreate(RoomUserBase):
    pass
