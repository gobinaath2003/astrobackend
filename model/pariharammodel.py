from database import db

class Pariharam(db.Model):
    __tablename__ = "pariharam"

    id = db.Column(db.Integer, primary_key=True)
    pariharamname = db.Column(db.String(100))
    notes = db.Column(db.String(200))