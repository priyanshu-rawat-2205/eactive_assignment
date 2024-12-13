from xmlrpc.client import Boolean
import mysql.connector
from config import CONFIG

# mysql connection without database

db = mysql.connector.connect(
    host=CONFIG.MYSQL_HOST,
    user=CONFIG.MYSQL_USER,
    password=CONFIG.MYSQL_PASSWORD,
)

db_cursor = db.cursor()

def db_exists() -> Boolean:
    db_cursor.execute("SHOW DATABASES;")
    result = db_cursor.fetchall()

    for i in result:
        if CONFIG.MYSQL_DB in i:
            return True
        
    return False

def setup_db():
    if db_exists():
        print(f"{CONFIG.MYSQL_DB} database already exists kindly use it as is or delete it first to create a new one")
        return
    else:
        db_cursor.execute("CREATE DATABASE users;")
        print(f"{CONFIG.MYSQL_DB} database created successfully")

def setup_table():

    # mysql connection with database
    user_db = mysql.connector.connect(
        host=CONFIG.MYSQL_HOST,
        user=CONFIG.MYSQL_USER,
        password=CONFIG.MYSQL_PASSWORD,
        db = CONFIG.MYSQL_DB
    )
    user_cursor = user_db.cursor()

    user_cursor.execute("SHOW TABLES;")
    res = user_cursor.fetchall()
    for i in res:
        if 'users' in i:
            print("users table already exists kindly delete that or use it as is")
            return
        
    user_cursor.execute("CREATE TABLE users (id int NOT NULL AUTO_INCREMENT, name varchar(255), email varchar(255), role varchar(255),  PRIMARY KEY (id));")
    print("table created successfully")
    return

if __name__ == '__main__':
    setup_db()
    setup_table()
