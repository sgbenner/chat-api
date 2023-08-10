from sqlalchemy.orm import Session

from app.models.room import Room
from app.schemas.rooms import RoomCreate


def get_room(db: Session, room_id: int):
    return db.query(Room).filter(Room.id == room_id).first()


def create_room(db: Session, room: RoomCreate):
    db_room = Room(
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
