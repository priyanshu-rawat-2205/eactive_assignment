from flask import Flask, jsonify
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
    result = cur.fetchall()
    cur.close()
    return jsonify(result)

