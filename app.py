from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello my friend nigga'

