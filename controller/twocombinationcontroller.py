from flask import request, jsonify
from model.twocombimation import twocombination
from database import db


# CREATE
def add_twocombination():
    data = request.json

    combo = twocombination(
        twocombination=data["twocombination"],
        notes=data["notes"]
    )

    db.session.add(combo)
    db.session.commit()

    return jsonify({"message": "twocombination added successfully"})


# GET ALL
def get_twocombination():
    combos = twocombination.query.all()

    result = []

    for c in combos:
        result.append({
            "id": c.id,
            "twocombination": c.twocombination,
            "notes": c.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_twocombination(id):
    combo = twocombination.query.get(id)

    if not combo:
        return jsonify({"message": "twocombination not found"}), 404

    return jsonify({
        "id": combo.id,
        "twocombination": combo.twocombination,
        "notes": combo.notes
    })


# UPDATE
def update_twocombination(id):
    data = request.json

    combo = twocombination.query.get(id)

    if not combo:
        return jsonify({"message": "twocombination not found"}), 404

    combo.twocombination = data["twocombination"]
    combo.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "twocombination updated successfully"})


# DELETE
def delete_twocombination(id):
    combo = twocombination.query.get(id)

    if not combo:
        return jsonify({"message": "twocombination not found"}), 404

    db.session.delete(combo)
    db.session.commit()

    return jsonify({"message": "twocombination deleted successfully"})