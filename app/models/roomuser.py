from sqlalchemy import ForeignKey, Column

from app.models._base import BasePlus


class RoomUser(BasePlus):
    # TODO: Permissions, Room Settings (private/public), etc.
    __tablename__ = "room_user"

    room = Column(ForeignKey("room.id"), primary_key=True)
    user = Column(ForeignKey("user.id"), primary_key=True)
