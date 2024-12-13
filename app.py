from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'this is the root of the api'

@app.route('/hello')
def hello():
    return 'hello world'

