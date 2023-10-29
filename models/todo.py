from typing import Any
from typing_extensions import Self

from sqlalchemy import String, Column, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Query

from extensions import db, ma
from models.base import Base


class TodoQuery(Query):
    def filter_by(self, **kwargs: Any) -> Self:
        if "deleted" not in kwargs:
            kwargs["deleted"] = None

        return super().filter_by(**kwargs)


class Todo(Base):
    __tablename__ = "todo_Todo"

    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True, default="")
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('auth_User.id'), nullable=False, index=True)
    user = db.relationship("User", backref='todo')

    query_class = TodoQuery


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = Todo
        fields = ("id", "title", "description", "is_done", "user_id")
        load_instance = True


todos_schema = TodoSchema(many=True, exclude=["user_id"])
edit_todo_schema = TodoSchema(dump_only=["id", ], exclude=["user_id"])
add_todo_schema = TodoSchema(load_only=["user_id"], dump_only=["is_done", "id"])
