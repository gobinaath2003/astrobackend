from database import db

class User(db.Model):
    __tablename__ = "rasi"

    id = db.Column(db.Integer, primary_key=True)
    lagnam = db.Column(db.String(100), unique=True)
    notes = db.Column(db.String(100))