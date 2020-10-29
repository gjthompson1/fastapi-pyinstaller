from sqlalchemy import Column, Integer, Boolean, String

from .meta import Meta

class Process(Meta):
    __tablename__ = "process"

    counter = Column(Integer)
    run_state = Column(String)
