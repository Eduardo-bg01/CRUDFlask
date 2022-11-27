from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(20))

class Usuarios(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.column(db.String(20))
    passwd = db.Column(db.String(20))