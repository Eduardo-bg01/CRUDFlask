from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Videojuegos(db.Model):
    __tablename__ = 'videojuegos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    noplayers = db.Column(db.Integer)