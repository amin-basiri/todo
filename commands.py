from flask_migrate.cli import db as db_cli
from sqlalchemy_utils import create_database, database_exists

from extensions import db

__all__ = tuple()


@db_cli.command("create")
def create():
    """ Create Database """

    if not database_exists(db.engine.url):
        create_database(db.engine.url)
        print(f"Database {db.engine.url.database} created.")

    else:
        print(f"Database {db.engine.url.database} already exists.")
