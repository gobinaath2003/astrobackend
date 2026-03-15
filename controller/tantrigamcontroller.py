from flask import request, jsonify
from model.tantrigammodel import Tantrigam
from database import db


# CREATE
def add_tantrigam():
    data = request.json

    tantrigam = Tantrigam(
        tantrigamname=data["tantrigamname"],
        notes=data["notes"]
    )

    db.session.add(tantrigam)
    db.session.commit()

    return jsonify({"message": "tantrigam added successfully"})


# GET ALL
def get_tantrigam():
    tantrigams = Tantrigam.query.all()

    result = []

    for t in tantrigams:
        result.append({
            "id": t.id,
            "tantrigamname": t.tantrigamname,
            "notes": t.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_tantrigam(id):
    tantrigam = Tantrigam.query.get(id)

    if not tantrigam:
        return jsonify({"message": "tantrigam not found"}), 404

    return jsonify({
        "id": tantrigam.id,
        "tantrigamname": tantrigam.tantrigamname,
        "notes": tantrigam.notes
    })


# UPDATE
def update_tantrigam(id):
    data = request.json

    tantrigam = Tantrigam.query.get(id)

    if not tantrigam:
        return jsonify({"message": "tantrigam not found"}), 404

    tantrigam.tantrigamname = data["tantrigamname"]
    tantrigam.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "tantrigam updated successfully"})


# DELETE
def delete_tantrigam(id):
    tantrigam = Tantrigam.query.get(id)

    if not tantrigam:
        return jsonify({"message": "tantrigam not found"}), 404

    db.session.delete(tantrigam)
    db.session.commit()

    return jsonify({"message": "tantrigam deleted successfully"})