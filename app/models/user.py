from sqlalchemy import Column, String, Boolean

from app.models._base import BasePlus

class User(BasePlus):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)
    # is_enabled = Column(Boolean, default=True)
    # last_login_time = Column(DateTime, default=datetime.utcnow)

    # rooms = relationship("Room", secondary="room_user", back_populates="users")
    # created_communities = relationship("Community", back_populates="creator")
    # communities = relationship("Community", secondary="community_users", back_populates="users")
