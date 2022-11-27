from app import create_app
from app.migrate import init_db
from flask import render_template, url_for, redirect, request
from app.models import *
app = create_app()


@app.route('/database')
def create_db():
    init_db()
    return "la base de datos ha sido creada"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        name_v = request.form['mail']
        ppl_v = request.form['passwd']

        videogame = Videojuegos(
            name = name_v,
            noplayers = ppl_v
        )

        db.session.add(videogame)
        db.session.commit()


        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/enlistar')
def enlistar():
    videojuegos = Videojuegos.query.filter(noplayers=5).first()
    print(videojuegos.name)

    for v in Videojuegos.query.all():
        print(v.name)

    return "test"

if __name__ == "__main__":
    app.run(debug=True, port=5000)