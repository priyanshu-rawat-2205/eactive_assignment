from flask import Flask, jsonify, redirect, render_template, request, flash, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_object('config.CONFIG')
app.secret_key = 'some secret'

mysql = MySQL(app)

@app.route('/')
def index():
    return 'welcome to the eactive assignment api'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/users')
def all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

@app.route('/users/<id>')
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {id}")
    user = cur.fetchall()
    cur.close()
    return jsonify(user)

@app.route('/new_user')
def new_user():
    return render_template('create_user.html')

@app.route('/new_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    role = request.form['role']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email, role) VALUE (%s, %s, %s)", (name, email, role))
    mysql.connection.commit()
    flash("user created successfully", "success")
    cur.close()

    return redirect(url_for('all_users'))

