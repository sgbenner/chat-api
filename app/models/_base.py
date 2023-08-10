from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, DateTime

from app.backend.session import Base


class BasePlus(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = Column(Boolean, default=False)
