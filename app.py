from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_object('config.CONFIG')

mysql = MySQL(app)

@app.route('/')
def index():
    return 'welcome to the eactive assignment api'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/users')
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

