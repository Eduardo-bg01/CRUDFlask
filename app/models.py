from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
<<<<<<< HEAD
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(20))

class Usuarios(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.column(db.String(20))
    passwd = db.Column(db.String(20))
=======
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Videojuegos(db.Model):
    __tablename__ = 'videojuegos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    noplayers = db.Column(db.Integer)
>>>>>>> af86ed3e86aa2656c59a8860b29965c80fc59832
