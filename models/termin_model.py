from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from main import db 


class Termin(db.Model):
    __tablename__ = 'termin'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(1000), nullable = False)
    time = db.Column(db.Integer(100), nullable = False)
    date = db.Column(db.Integer(100), nullable = False)
    description = db.Column(db.String(8000), nullable = False)