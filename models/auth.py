from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import ma
from models.base import Base


class User(Base):
    __tablename__ = "auth_User"

    full_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = generate_password_hash(self.password)

    def is_password_ok(self, password):
        return check_password_hash(self.password, password)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("username", "full_name", "password")
        load_instance = True


sign_up_schema = UserSchema(load_only=["password", ])
sign_in_schema = UserSchema(exclude=["full_name", ], load_instance=False)
