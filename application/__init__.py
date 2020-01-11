import os
from flask import Flask
from .app import main_bp

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    env = os.environ.get('FLASK_ENV')

    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    elif env == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    app.register_blueprint(main_bp)
    return app