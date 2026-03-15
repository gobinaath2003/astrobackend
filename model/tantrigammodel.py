from database import db

class Tantrigam(db.Model):
    __tablename__ = "tantrigam"

    id = db.Column(db.Integer, primary_key=True)
    tantrigamname = db.Column(db.String(100))
    notes = db.Column(db.String(200))