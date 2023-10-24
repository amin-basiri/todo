class BaseConfig:
    SQLALCHEMY_DATABASE_URI = NotImplemented
    SECRET_KEY = NotImplemented


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:amin_123@localhost:5432/todo"
    SECRET_KEY = "admfgnhahl^nd$l@andw(64a6d()63#$#sefesf66448321sfsef64486^5ry5yrrY%r"
