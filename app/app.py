from app import create_app
from flask import render_template, request, redirect, session
from app.migrate import init_db
from flask_mysqldb import MySQL
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
    idBorrar = request.form.get("nombreBorrar")
    foundProducto = Productos.query.filter_by(idBorrar=idBorrar).first()
    db.session.delete(foundProducto)
    db.session.commit()

    productos = Productos.query.all()
    return render_template('home.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)