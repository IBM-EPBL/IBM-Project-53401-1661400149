from flask import Flask;
from flask import render_template;

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('login.html')

@app.route('/signup')
def show():
    return render_template('register.html')