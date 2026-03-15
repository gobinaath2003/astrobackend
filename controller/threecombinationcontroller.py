from flask import request, jsonify
from model.threecombinationmodel import ThreeCombination
from database import db


# CREATE
def add_threecombination():
    data = request.json

    combo = ThreeCombination(
        threecombination=data["threecombination"],
        notes=data["notes"]
    )

    db.session.add(combo)
    db.session.commit()

    return jsonify({"message": "three combination added successfully"})


# GET ALL
def get_threecombination():
    combos = ThreeCombination.query.all()

    result = []

    for c in combos:
        result.append({
            "id": c.id,
            "threecombination": c.threecombination,
            "notes": c.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_threecombination(id):
    combo = ThreeCombination.query.get(id)

    if not combo:
        return jsonify({"message": "three combination not found"}), 404

    return jsonify({
        "id": combo.id,
        "threecombination": combo.threecombination,
        "notes": combo.notes
    })


# UPDATE
def update_threecombination(id):
    data = request.json

    combo = ThreeCombination.query.get(id)

    if not combo:
        return jsonify({"message": "three combination not found"}), 404

    combo.threecombination = data["threecombination"]
    combo.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "three combination updated successfully"})


# DELETE
def delete_threecombination(id):
    combo = ThreeCombination.query.get(id)

    if not combo:
        return jsonify({"message": "three combination not found"}), 404

    db.session.delete(combo)
    db.session.commit()

    return jsonify({"message": "three combination deleted successfully"})