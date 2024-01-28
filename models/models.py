from models import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(1000), nullable = False)
    lastName = db.Column(db.String(1000), nullable = False)
    email = db.Column(db.String(6000), nullable = False)

class Termin(db.Model):
    __tablename__ = 'termin'
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(1000), nullable = False)
    location = db.Column(db.String(1000), nullable = False)
    time = db.Column(db.Integer, nullable = False)
    date = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(8000), nullable = False)
