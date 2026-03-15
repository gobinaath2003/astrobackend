from database import db

class twocombination(db.Model):
    __tablename__ = "twocombination"

    id = db.Column(db.Integer, primary_key=True)
    twocombination = db.Column(db.String(100))
    notes = db.Column(db.String(200))