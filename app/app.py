from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import config


#models
from models.ModelUser import ModelUser
#entities
from models.entities.User import User

app=Flask(__name__)
db=MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()