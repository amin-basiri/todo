import os
from flask import Flask
from importlib import import_module

import config
import models # noqa

apps = ['auth', 'todo']


def config_extensions(application: Flask):
    import extensions

    for extension in extensions.__all__:
        getattr(extensions, extension).init_app(application)


def config_blueprints(application: Flask):
    for app_name in apps:
        bp = import_module(f"{app_name}.{app_name}")
        application.register_blueprint(bp.bp)


def config_cli_commands(application: Flask):
    import commands

    for command in commands.__all__:
        application.cli.add_command(getattr(commands, command))


def get_configuration_object():
    env = os.getenv('FLASK_ENV') or 'production'

    if env == 'development':
        configuration = config.DevelopmentConfig()
    else:
        raise NotImplementedError()

    return configuration


def create_app():
    config_obj = get_configuration_object()

    application = Flask(__name__)
    application.config.from_object(config_obj)
    config_blueprints(application)
    config_extensions(application)
    config_cli_commands(application)

    return application


if __name__ == '__main__':
    app = create_app()
    app.run()
