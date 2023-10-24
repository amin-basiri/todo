from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

__all__ = ('db', 'migrate', 'ma')


db = SQLAlchemy()
migrate = Migrate(db=db)
ma = Marshmallow()
