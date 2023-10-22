import os
from importlib import import_module

import todo
import config
from flask import Flask

apps = ['auth', 'todo']


def config_extensions(app: Flask):
    import extensions

    for extension in extensions.__all__:
        getattr(extensions, extension).init_app(app)


def config_blueprints(app: Flask):
    for app_name in apps:
        bp = import_module(f"{app_name}.{app_name}")
        app.register_blueprint(bp.bp)


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    config_blueprints(app)
    config_extensions(app)

    return app


if __name__ == '__main__':
    env = os.getenv('FLASK_ENV') or 'production'

    if env == 'development':
        configuration = config.DevelopmentConfig()
    else:
        raise NotImplementedError()

    flask_app = create_app(configuration)
    flask_app.run()
