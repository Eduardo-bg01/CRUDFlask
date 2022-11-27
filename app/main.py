from app import create_app
from flask import render_template, request, redirect, url_for, session
from app.models import *

app = create_app()


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['mail']
        contra = request.form['passwd']

        us = Usuarios(mail=correo, passwd=contra)

        db.session.add(us)
        db.session.commit()
        return render_template('login.html')
    else:
        return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
