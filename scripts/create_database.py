from xmlrpc.client import Boolean
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""

)

cursor = db.cursor()

def db_exists() -> Boolean:
    cursor.execute("SHOW DATABASES;")
    result = cursor.fetchall()

    for i in result:
        if 'users' in i:
            return True
        
    return False

if db_exists():
    print("users database already exists kindly use it as is or delete it first to create a new one")
else:
    cursor.execute("CREATE DATABASE users;")
    print("users database created successfully")

