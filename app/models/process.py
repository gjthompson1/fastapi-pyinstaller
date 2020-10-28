from sqlalchemy import Column, Integer, Boolean

from .meta import Meta

class Process(Meta):
    __tablename__ = "process"

    counter = Column(Integer)
    canceled = Column(Boolean, default=False)
