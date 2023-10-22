class BaseConfig:
    SQLALCHEMY_DATABASE_URI = NotImplemented


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:amin@123@localhost:5432/todo"
