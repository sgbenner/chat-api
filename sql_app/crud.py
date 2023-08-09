import uuid

from sqlalchemy.orm import Session

from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_password_hash(db: Session, email: str):
    return db.query(models.User.hashed_password).filter(models.User.email == email).first()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_room(db: Session, room_id: int):
    return db.query(models.Room).filter(models.Room.id == room_id).first()


def get_user_rooms(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    # user_rooms = db.query(models.RoomUser).filter(models.RoomUser.user_id == user_id).offset(skip).limit(limit).all()
    return db.query(models.RoomUser).filter(models.RoomUser.user_id == user_id).offset(skip).limit(limit).all()


## Rooms
def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(
        title=room.title,
        description=room.description,
        type=room.type,
        creator=room.creator,  # TODO: Update to use current user once auth set up
        settings=room.settings,
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# def get_user_rooms(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.RoomUser).offset(skip).limit(limit).all()
