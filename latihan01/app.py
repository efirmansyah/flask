from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World, Dilo Bandung'

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hi')
def hi():
    return 'Hi, Everyone, whats up?'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username











