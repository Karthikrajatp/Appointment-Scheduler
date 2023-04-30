from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    userdesignation = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    phonenumber = db.Column(db.String(20))
    password = db.Column(db.String(50))
    availability=db.Column(db.Boolean,default=True)

class Appointments(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    host_email = db.Column(db.String(50))
    guest_email = db.Column(db.String(50))
    title = db.Column(db.String(50))
    agenda = db.Column(db.String(100))
    time = db.Column(db.DateTime)
    