from database import db

class Mantrigam(db.Model):
    __tablename__ = "mantrigam"

    id = db.Column(db.Integer, primary_key=True)
    mantrigamname = db.Column(db.String(100))
    notes = db.Column(db.String(200))