from models import db

class Termin(db.Model):
    __tablename__ = 'termin'
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(1000), nullable = False)
    location = db.Column(db.String(1000), nullable = False)
    time = db.Column(db.Integer, nullable = False)
    date = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(8000), nullable = False)
