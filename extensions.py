from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

__all__ = ('db', 'migrate', 'ma', 'jwt')


db = SQLAlchemy()
migrate = Migrate(db=db)
ma = Marshmallow()
jwt = JWTManager()
