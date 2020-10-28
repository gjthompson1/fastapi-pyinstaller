from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .meta import Meta

class User(Meta):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
