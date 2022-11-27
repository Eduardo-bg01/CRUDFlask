import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from config import config

app=Flask(__name__)
db=MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'mail' in request.form and 'passwd' in request.form:
        mail = request.form['mail']
        passwd = request.form['passwd']
        cursor = MySQLdb.MySQLError.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE mail = %s AND passwd = %s', (mail, passwd,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['mail'] = account['mail']
            return 'Logged in successfully!'
        else:
            msg = 'Incorrect username/password!'
    return render_template('home.html', msg=msg)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()