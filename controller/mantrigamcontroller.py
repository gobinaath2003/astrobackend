from flask import request, jsonify
from model.mantrigammodel import Mantrigam
from database import db


# CREATE
def add_mantrigam():
    data = request.json

    mantrigam = Mantrigam(
        mantrigamname=data["mantrigamname"],
        notes=data["notes"]
    )

    db.session.add(mantrigam)
    db.session.commit()

    return jsonify({"message": "mantrigam added successfully"})


# GET ALL
def get_mantrigam():
    mantrigams = Mantrigam.query.all()

    result = []

    for m in mantrigams:
        result.append({
            "id": m.id,
            "mantrigamname": m.mantrigamname,
            "notes": m.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_mantrigam(id):
    mantrigam = Mantrigam.query.get(id)

    if not mantrigam:
        return jsonify({"message": "mantrigam not found"}), 404

    return jsonify({
        "id": mantrigam.id,
        "mantrigamname": mantrigam.mantrigamname,
        "notes": mantrigam.notes
    })


# UPDATE
def update_mantrigam(id):
    data = request.json

    mantrigam = Mantrigam.query.get(id)

    if not mantrigam:
        return jsonify({"message": "mantrigam not found"}), 404

    mantrigam.mantrigamname = data["mantrigamname"]
    mantrigam.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "mantrigam updated successfully"})


# DELETE
def delete_mantrigam(id):
    mantrigam = Mantrigam.query.get(id)

    if not mantrigam:
        return jsonify({"message": "mantrigam not found"}), 404

    db.session.delete(mantrigam)
    db.session.commit()

    return jsonify({"message": "mantrigam deleted successfully"})