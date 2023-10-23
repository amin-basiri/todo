from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

__all__ = ('db', 'migrate')


db = SQLAlchemy()
migrate = Migrate(db=db)
