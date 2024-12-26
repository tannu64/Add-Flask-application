from flask import Flask
from app.routes import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration

    # Register blueprints
    app.register_blueprint(api_blueprint)

    return app
