from models import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(1000), nullable = False)
    lastName = db.Column(db.String(1000), nullable = False)
    email = db.Column(db.String(6000), nullable = False)