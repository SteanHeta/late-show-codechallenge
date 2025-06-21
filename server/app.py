from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from dotenv import load_dotenv
import os

from models import db
from controllers.episode_controller import episode_bp
from controllers.guest_controller import guest_bp
from controllers.appearance_controller import appearance_bp
from controllers.auth_controller import auth_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)
    app.register_blueprint(auth_bp)

    return app

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
