from flask import Flask, render_template, request, redirect, url_for, session
#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from config import config

app=Flask(__name__)
db=SQLAlchemy(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/agregarProducto", methods=["GET", "POST"])
def agregarProducto():
    producto = None
    if request.form:
        try:
            nombre = producto(nombre=request.form.get("nombreProducto"))
            precio = producto(precio=request.form.get("precioProducto"))
            cantidad = producto(cantidad=request.form.get("cantidadProducto"))
            db.session.add(nombre, precio, cantidad)
            db.session.commit
        except Exception as e:
            print("Fallo al agregar prodcuto")
            print(e)
    productos = producto.query.all()
    return render_template('home.html', productos=productos)
    
@app.route("/actualizarNombreProducto", methods=["POST"])
def actualizarNombreProducto():
    try:
        nombreNuevo = request.form.get("nombreNuevo")
        nombreViejo = request.form.get("nombreViejo")
        producto = producto.query.filter_by(nombre=nombreViejo).first()
        producto.nombre = nombreNuevo
        db.session.commit()
    except Exception as e:
        print("No se pudo actualizar el nombre")
        print(e)
    return redirect("home.html")

@app.route("/actualizarPrecioProducto", methods=["POST"])
def actualizarPrecioProducto():
    try:
        precioNuevo = request.form.get("precioNuevo")
        precioViejo = request.form.get("precioViejo")
        producto = producto.query.filter_by(precio=precioViejo).first()
        producto.precio = precioNuevo
        db.session.commit()
    except Exception as e:
        print("No se pudo actualizar el precio")
        print(e)
    return redirect("home.html")

@app.route("/actualizarCantidadProducto", methods=["POST"])
def actualizarCantidadProducto():
    try:
        cantidadNuevo = request.form.get("cantidadNuevo")
        cantidadViejo = request.form.get("cantidadejo")
        producto = producto.query.filter_by(cantidad=cantidadViejo).first()
        producto.cantidad = cantidadNuevo
        db.session.commit()
    except Exception as e:
        print("No se pudo actualizar la cantidad")
        print(e)
    return redirect("home.html")


@app.route("/borrarProducto", methods=["POST"])
def delete():
    nombreBorrar = request.form.get("nombreBorrar")
    producto = producto.query.filter_by(nombreBorrar=nombreBorrar).first()
    db.session.delete(producto)
    db.session.commit()
    return render_template('home.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()