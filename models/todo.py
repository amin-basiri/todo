from sqlalchemy import String, Column, Text, Boolean, DateTime

from models.base import Base


class Todo(Base):
    __tablename__ = "todo_Todo"

    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True, default="")
    is_done = Column(Boolean, default=False)
