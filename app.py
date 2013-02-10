from flask import Flask
from config import DevConfig, ProdConfig
from extensions import db
from os import getenv

def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object(DevConfig)
    if config is not None:
        app.config.from_object(config)

    db.init_app(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from home.views import home

    for blueprint in (home, ):
        app.register_blueprint(blueprint)

if getenv('PORT'):
    port = int(getenv('PORT'))
    app = create_app(ProdConfig)
else:
    port = 5000
    app = create_app()


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")