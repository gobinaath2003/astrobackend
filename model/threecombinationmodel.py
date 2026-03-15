from database import db

class ThreeCombination(db.Model):
    __tablename__ = "threecombination"

    id = db.Column(db.Integer, primary_key=True)
    threecombination = db.Column(db.String(100))
    notes = db.Column(db.String(200))