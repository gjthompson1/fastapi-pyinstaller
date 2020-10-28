from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime

from app.database import SessionLocal

class Meta(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)

    def save(self, session=None):
        self.updated_at = datetime.utcnow()
        if not session:
            session = SessionLocal()
        session.add(self)
        return self

    def delete(self, session=None):
        self.updated_at = datetime.utcnow()
        if not session:
            session = SessionLocal()
        session.delete(self)
        return self

    def __repr__(self):
        id = self.id if self.id else None
        return f'<{self.__class__.__name__} {id}>'
