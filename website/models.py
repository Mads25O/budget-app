from . import db

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(150))
    amount = db.Column(db.Integer)
    date = db.Column(db.String(150))
    re

class Subscriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)