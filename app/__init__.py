from flask import Flask
from app.config import Config
from app.models import db

<<<<<<< HEAD
def create_app():
    app =Flask(__name__)
=======

def create_app():
    app = Flask(__name__)
>>>>>>> af86ed3e86aa2656c59a8860b29965c80fc59832
    app.config.from_object(Config)
    db.init_app(app)
    return app