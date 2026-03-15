from flask import request, jsonify
from model.rasimodel import User
from database import db


# CREATE
def add_lagnam():
    data = request.json

    user = User(
        lagnam=data["lagnam"],
        notes=data["notes"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "lagnam added successfully"})


# GET ALL
def get_lagnam():
    users = User.query.all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "lagnam": user.lagnam,
            "notes": user.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_lagnam(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "lagnam not found"}), 404

    return jsonify({
        "id": user.id,
        "lagnam": user.lagnam,
        "notes": user.notes
    })


# UPDATE
def update_lagnam(id):
    data = request.json

    user = User.query.get(id)

    if not user:
        return jsonify({"message": "lagnam not found"}), 404

    user.lagnam = data["lagnam"]
    user.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "lagnam updated successfully"})


# DELETE
def delete_lagnam(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "lagnam not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "lagnam deleted successfully"})