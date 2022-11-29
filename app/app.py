from app import create_app
from flask import render_template, request, redirect, session
from app.migrate import init_db
from app.models import *

app= create_app()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'mail' in request.form and 'passwd' in request.form:

        mail = request.form['mail']
        passwd = request.form['passwd']

        mail = Usuarios.query.filter_by(mail=mail).first()
        if mail != None:
            mail = Usuarios.query.filter_by(passwd=passwd).first()

            if mail != None:
                productos = Productos.query.all()
                return render_template('home.html', productos = productos)
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/agregarProducto", methods=["GET", "POST"])
def agregarProducto():
    nombreP=request.form["nombre"]
    precioP=request.form["precio"]
    cantidadP=request.form["cantidad"]

    produ = Productos(nombre=nombreP,precio=precioP,cantidad=cantidadP)

    db.session.add(produ)
    db.session.commit()
    
    productos = Productos.query.all()
    return render_template('home.html', productos=productos)
    
@app.route("/actualizarNombreProducto", methods=["POST"])
def actualizarNombreProducto():
        nombrePN= request.form.get("nombreNuevo")
        nombrePV = request.form.get("nombreViejo")

        produ = Productos.query.filter_by(nombre=nombrePV).first()
        produ.nombre = nombrePN
        db.session.commit()

        productos = Productos.query.all()
        return render_template('home.html', productos=productos)

@app.route("/actualizarPrecioProducto", methods=["POST"])
def actualizarPrecioProducto():

        precioPN = request.form.get("precioNuevo")
        precioPV = request.form.get("precioViejo")

        produ = Productos.query.filter_by(precio=precioPV).first()
        produ.precio = precioPN
        db.session.commit()

        productos = Productos.query.all()
        return render_template('home.html', productos=productos)

@app.route("/actualizarCantidadProducto", methods=["POST"])
def actualizarCantidadProducto():
        cantidadPN = request.form.get("cantidadNuevo")
        cantidadPV = request.form.get("cantidadejo")

        produ = Productos.query.filter_by(cantidad=cantidadPV).first()
        produ.cantidad = cantidadPN
        db.session.commit()

        productos = Productos.query.all()
        return render_template('home.html', productos=productos)


@app.route("/borrarProducto", methods=["POST"])
def delete():
    idBorrar = request.form.get("nombreBorrar")
    fProducto = Productos.query.filter_by(idproducto=idBorrar).first()
    db.session.delete(fProducto)
    db.session.commit()

    productos = Productos.query.all()
    return render_template('home.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)