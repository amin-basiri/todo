from sqlalchemy.sql import func
from sqlalchemy import Column, TIMESTAMP, Integer

from extensions import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP, nullable=True, onupdate=func.current_timestamp())
    deleted = Column(TIMESTAMP, nullable=True)
