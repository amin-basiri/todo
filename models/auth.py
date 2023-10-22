from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash, check_password_hash

from models.base import Base


class User(Base):
    full_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = generate_password_hash(self.password)
