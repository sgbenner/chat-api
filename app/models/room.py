from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.models._base import BasePlus


class Room(BasePlus):
    __tablename__ = "room"

    title = Column(String)
    description = Column(String)
    type = Column(String)
    creator = Column(Integer, ForeignKey("user.id"))
    settings = Column(JSON)

    users = relationship("User", secondary="room_user", back_populates="rooms")
