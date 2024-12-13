## Prerequisite:

### mysql server must be installed
- refer to the mysql documentation for installation instruction

### linux environment
- this api is built in a linux environment it is recommended to use a similar environment
- if not then kindly access installation instruction according to you system for each dependency

**mysql-connector-python package require addition libraries therefore run:**

```bash
$ sudo apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential
```

To install rest of the dependencies run:
```bash
$ pip install -r requirements.txt
```

now to setup and seed the database run the `create_database.py` script like this:

```bash
$ python create_database.py
```

### Configuration
you must configure your database credentials in `config.py` eg:

```python
class CONFIG:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'users'
    MYSQL_CURSORCLASS = 'DictCursor'
```

## Usage

After Successfull completion of [these steps](#prerequisite) run below command to launch the serve

```bash
$ flask run
```

the server should boot-up on `localhost:5000`

to access the below routes just append them after the above address like `localhost:5000/hello` and put it in a browsers search bar

*Note: Most of the routes return templates due to which api testing tools might not functon properly although I've not tested them

## Available Routes

- `/` shows the index
- `/hello` returns hello
- `/users` returns a list of all the user in html
- `/new_user` shows a form to create new users
- `/users/<id>` shows the user by id eg: `/users/1`

## Approach

- I've used bootstrap to make a decent UI
- I've not used any ORM so that raw sql query can be displayed if it was mentioned in the assignment spec i would've used
- i used two different mysql driver one for running the `create_database` script that is `mysql-connector-python` and `flask-mysqldb` for ease of use in flask
- as usual jinja templates are used

### SQL Queries
- **Inserting**: 
   I've used prepared statements for security even though it's not enough
```sql 
INSERT INTO users (name, email, role) VALUE (%s, %s, %s)
```


- **Retrieve all Users**
  
```sql
SELECT * FROM users
```

- **Retrieve a specific user by id**

```sql
SELECT * FROM users WHERE id = %s"
```

### SQL Schema
the schema is written in the `create_database.py` script

```sql
CREATE TABLE users (id int NOT NULL AUTO_INCREMENT, name varchar(255), email varchar(255), role varchar(255),  PRIMARY KEY (id));
```


## Contribution

If you want to contribute to the project 

kindly fork the repo create a branch named as `your_feature` after completing send a pull request and hopefully we'll merge it in :)


I hope i've not missed anything else