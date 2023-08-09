import types
from datetime import datetime

from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class BasePlus(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = Column(Boolean, default=False)


# Every community will have their own subscription. You have to be invited into a subscription. A subscription will have a subscription owner


# class Community(Base):
#     __tablename__ = "community"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)
#     creator_user_id = Column(Integer, ForeignKey("users.id"))
#     settings = Column(types.JSON)
#
#     creator = relationship("User", back_populates="created_communities")
#
# community_users = Table(
#     "community_user",
#     Base.metadata,
#     Column("user_id", Integer, ForeignKey("users.id")),
#     Column("room_id", Integer, ForeignKey("room.id")),
# )
#
#
# class CommunityMember(Base):
#     # can store info in this table about community permissions and settings
#     __tablename__ = "community_member"
#
#     id = Column(String, primary_key=True, index=True)
#     user = Column(Integer, ForeignKey("users.id"))
#     community = Column(Integer, ForeignKey("community.id"))
#
#     communities = relationship("Community", back_populates="users")

class User(BasePlus):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)
    # is_enabled = Column(Boolean, default=True)
    # last_login_time = Column(DateTime, default=datetime.utcnow)

    rooms = relationship("Room", secondary="room_user", back_populates="users")
    # created_communities = relationship("Community", back_populates="creator")
    # communities = relationship("Community", secondary="community_users", back_populates="users")


class Room(BasePlus):
    __tablename__ = "room"

    title = Column(String)
    description = Column(String)
    type = Column(String)
    creator = Column(Integer, ForeignKey("user.id"))
    settings = Column(JSON)

    users = relationship("User", secondary="room_user", back_populates="rooms")


class RoomUser(BasePlus):
    # TODO: Permissions, Room Settings (private/public), etc.
    __tablename__ = "room_user"

    room = Column(ForeignKey("room.id"), primary_key=True)
    user = Column(ForeignKey("user.id"), primary_key=True)

# class Message(Base):
#     __tablename__ = "message"
#
#     message = Column(String, index=True)
#     room = Column(Integer, ForeignKey("room.id"))
#     creator = Column(Integer, ForeignKey("users.id"))
