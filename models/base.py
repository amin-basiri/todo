from sqlalchemy.sql import func
from sqlalchemy import Column, TIMESTAMP, Integer

from extensions import db


class Base(db.Model):
    def __tablename__(self):
        return f"{__package__}_{self.__class__.__name__}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP, nullable=True, onupdate=func.current_timestamp())
    deleted = Column(TIMESTAMP, nullable=True)
