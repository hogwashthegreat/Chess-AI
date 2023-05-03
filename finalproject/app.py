

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import requests
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql.2223.lakeside-cs.org'
app.config['MYSQL_USER'] = 'student2223'
app.config['MYSQL_PASSWORD'] = 'm545CS42223'
app.config['MYSQL_DB'] = '2223project_1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'jsdkahfueobaljcbijeabcidabkj'
mysql = MySQL(app)

@app.route('/')
def index():
    if not (session.get('troymerritt_username')):
        error=0
        return render_template('index.html.j2', error = error)
    else:
        return redirect(url_for('mainpage'))


@app.route('/results')                                                                                                  
def results():
    cursor = mysql.connection.cursor()
    username = request.values.get("username")
    password = request.values.get("pw")
    securepw = generate_password_hash(password)
    if (len(username) < 6 or len(password) < 8):
        print("failure")
    else:
        query = "SELECT * FROM troymerritt_users WHERE username = %s;"
        queryVars = (username, )
        cursor.execute(query, queryVars)
        mysql.connection.commit()
        data=cursor.fetchall()
        if (len(data) == 0):
            query = "INSERT INTO troymerritt_users (username, password, score) VALUES  (%s ,%s, %s);"
            queryVars = (username,securepw,0, )
            cursor.execute(query, queryVars)
            mysql.connection.commit()
            data2=cursor.fetchall()
            failure = 0
        else:
            failure = 1
    return render_template('results.html.j2', username = username, password = password, failure = failure)

@app.route('/signup')
def signup():
    return render_template('signup.html.j2')


@app.route('/logout')
def logout():
    session.pop('troymerritt_username', None)
    return redirect(url_for('index'))

@app.route('/logoutconfirmation')
def logoutconfirmation():
    return render_template('signup.html.j2')

@app.route('/mainpage', methods = ["POST"])
def mainpage():
    return render_template('mainpage.html.j2')
