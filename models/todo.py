from sqlalchemy import String, Column, Text, Boolean, Integer, ForeignKey

from extensions import db, ma
from models.base import Base


class Todo(Base):
    __tablename__ = "todo_Todo"

    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True, default="")
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('auth_User.id'), nullable=False, index=True)
    user = db.relationship("User", backref='todo')


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = Todo
        fields = ("id", "title", "description", "is_done", "user_id")
        load_instance = True


add_todo_schema = TodoSchema(load_only=["user_id"], dump_only=["is_done", "id"])
