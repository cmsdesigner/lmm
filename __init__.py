from flask import Flask
from lmm.config import DevConfig
from lmm.extensions import db

def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object(DevConfig)
    if config is not None:
        app.config.from_object(config)

    db.init_app(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from lmm.home.views import home

    for blueprint in (home, ):
        app.register_blueprint(blueprint)


if __name__ == '__main__':
    app = create_app()
    app.run()