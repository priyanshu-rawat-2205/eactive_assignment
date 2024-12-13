from flask import Flask, redirect, render_template, request, url_for
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
def all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

@app.route('/users/<id>')
def get_user(id):
    cur = mysql.connection.cursor()

    try:
        cur.execute("SELECT * FROM users WHERE id = %s", id)
        user = cur.fetchall()
    except Exception as e:
        print(f"error {e}")
    finally:
        cur.close()

    return render_template('user.html', users=user)

@app.route('/new_user')
def new_user():
    return render_template('create_user.html')

@app.route('/new_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    role = request.form['role']

    cur = mysql.connection.cursor()

    try:

        cur.execute("INSERT INTO users (name, email, role) VALUE (%s, %s, %s)", (name, email, role))
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
        print(f"error: {e}")
    finally:
        cur.close()

    return redirect(url_for('all_users'))

