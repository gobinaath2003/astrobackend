from flask import request, jsonify
from model.bhavammodel import Bhavam
from database import db


# CREATE
def add_bhavam():
    data = request.json

    bhavam = Bhavam(
        bhavamname=data["bhavamname"],
        notes=data["notes"]
    )

    db.session.add(bhavam)
    db.session.commit()

    return jsonify({"message": "bhavam added successfully"})


# GET ALL
def get_bhavam():
    bhavams = Bhavam.query.all()

    result = []

    for b in bhavams:
        result.append({
            "id": b.id,
            "bhavamname": b.bhavamname,
            "notes": b.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_bhavam(id):
    bhavam = Bhavam.query.get(id)

    if not bhavam:
        return jsonify({"message": "bhavam not found"}), 404

    return jsonify({
        "id": bhavam.id,
        "bhavamname": bhavam.bhavamname,
        "notes": bhavam.notes
    })


# UPDATE
def update_bhavam(id):
    data = request.json

    bhavam = Bhavam.query.get(id)

    if not bhavam:
        return jsonify({"message": "bhavam not found"}), 404

    bhavam.bhavamname = data["bhavamname"]
    bhavam.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "bhavam updated successfully"})


# DELETE
def delete_bhavam(id):
    bhavam = Bhavam.query.get(id)

    if not bhavam:
        return jsonify({"message": "bhavam not found"}), 404

    db.session.delete(bhavam)
    db.session.commit()

    return jsonify({"message": "bhavam deleted successfully"})