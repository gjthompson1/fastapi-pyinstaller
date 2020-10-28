from sqlalchemy import Column, Integer, Boolean

from .meta import Meta

class Process(Meta):
    __tablename__ = "process"

    counter = Column(Integer, index=True)
    canceled = Column(Boolean, index=True)
