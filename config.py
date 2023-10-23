class BaseConfig:
    SQLALCHEMY_DATABASE_URI = NotImplemented


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:amin_123@localhost:5432/todo"
