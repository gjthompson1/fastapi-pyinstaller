from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .meta import Meta

class Item(Meta):
    __tablename__ = "items"

    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
