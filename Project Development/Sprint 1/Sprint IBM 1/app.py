from flask import Flask;
from flask import render_template;

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('home.html')

@app.route('/signup')
def singup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('loginpage.html')