from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func

from app.db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    events = relationship("Event", back_populates="owner", cascade="all, delete")

    invites = relationship("EventInvite", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"
