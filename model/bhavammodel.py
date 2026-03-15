from database import db

class Bhavam(db.Model):
    __tablename__ = "bhavam"

    id = db.Column(db.Integer, primary_key=True)
    bhavamname = db.Column(db.String(100), unique=True)
    notes = db.Column(db.String(200))