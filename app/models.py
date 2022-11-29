from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'tienda'
    iduser = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(20))
    passwd = db.Column(db.String(20))

class Productos(db.Model):
    __tablename__ = 'producto'
    idproducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    precio = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)