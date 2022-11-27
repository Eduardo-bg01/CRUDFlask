from flask import Flask
from app.config import Config
from app.models import db

def create_app():
    app =Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app