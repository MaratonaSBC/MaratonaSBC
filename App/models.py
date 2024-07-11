from app import db

class LoginData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
