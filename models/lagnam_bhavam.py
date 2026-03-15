from datetime import datetime
from bson.objectid import ObjectId
from bson.errors import InvalidId
from config.database import get_db

class LagnamBhavam:
    def __init__(self, data):
        self.lagnam_name = data.get('lagnam_name')
        self.bhavam_number = data.get('bhavam_number')
        self.bhavam_name = data.get('bhavam_name')
        self.planet_lord = data.get('planet_lord')
        self.description = data.get('description')
        self.characteristics = data.get('characteristics', [])
        self.strengths = data.get('strengths', [])
        self.weaknesses = data.get('weaknesses', [])
        self.remedies = data.get('remedies', [])
        self.compatibility = data.get('compatibility', {})
        self.created_at = data.get('created_at', datetime.utcnow())
        self.updated_at = data.get('updated_at', datetime.utcnow())
        self._id = data.get('_id')
    
    def to_dict(self):
        return {
            '_id': str(self._id) if self._id else None,
            'lagnam_name': self.lagnam_name,
            'bhavam_number': self.bhavam_number,
            'bhavam_name': self.bhavam_name,
            'planet_lord': self.planet_lord,
            'description': self.description,
            'characteristics': self.characteristics,
            'strengths': self.strengths,
            'weaknesses': self.weaknesses,
            'remedies': self.remedies,
            'compatibility': self.compatibility,
            'created_at': self.created_at.isoformat() if hasattr(self.created_at, 'isoformat') else str(self.created_at),
            'updated_at': self.updated_at.isoformat() if hasattr(self.updated_at, 'isoformat') else str(self.updated_at)
        }
    
    def to_mongo_doc(self):
        return {
            'lagnam_name': self.lagnam_name,
            'bhavam_number': self.bhavam_number,
            'bhavam_name': self.bhavam_name,
            'planet_lord': self.planet_lord,
            'description': self.description,
            'characteristics': self.characteristics,
            'strengths': self.strengths,
            'weaknesses': self.weaknesses,
            'remedies': self.remedies,
            'compatibility': self.compatibility,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# CRUD Operations
def create_lagnam_bhavam(lagnam_data):
    lagnam = LagnamBhavam(lagnam_data)
    db = get_db()
    result = db.lagnam_bhavam.insert_one(lagnam.to_mongo_doc())
    lagnam._id = result.inserted_id
    return lagnam

def get_lagnam_bhavam_by_id(lagnam_id):
    try:
        db = get_db()
        lagnam_data = db.lagnam_bhavam.find_one({'_id': ObjectId(lagnam_id)})
        return LagnamBhavam(lagnam_data) if lagnam_data else None
    except InvalidId:
        return None

def get_lagnam_bhavam_by_lagnam(lagnam_name):
    db = get_db()
    lagnams = list(db.lagnam_bhavam.find({'lagnam_name': lagnam_name}))
    return [LagnamBhavam(data) for data in lagnams]

def get_lagnam_bhavam_by_bhavam(bhavam_number):
    db = get_db()
    lagnams = list(db.lagnam_bhavam.find({'bhavam_number': bhavam_number}))
    return [LagnamBhavam(data) for data in lagnams]

def get_all_lagnam_bhavam():
    db = get_db()
    lagnams = list(db.lagnam_bhavam.find())
    return [LagnamBhavam(data) for data in lagnams]

def update_lagnam_bhavam(lagnam_id, update_data):
    try:
        update_data['updated_at'] = datetime.utcnow()
        db = get_db()
        result = db.lagnam_bhavam.update_one(
            {'_id': ObjectId(lagnam_id)},
            {'$set': update_data}
        )
        return result.modified_count > 0
    except InvalidId:
        return False

def delete_lagnam_bhavam(lagnam_id):
    try:
        db = get_db()
        result = db.lagnam_bhavam.delete_one({'_id': ObjectId(lagnam_id)})
        return result.deleted_count > 0
    except InvalidId:
        return False
