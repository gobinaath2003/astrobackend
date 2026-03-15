from flask import request, jsonify
from model.rasimodel import User
from database import db


# CREATE
def add_rasi():
    data = request.json

    user = User(
        rasiname=data["rasiname"],
        notes=data["notes"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "rasi added successfully"})


# GET ALL
def get_rasi():
    users = User.query.all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "rasiname": user.rasiname,
            "notes": user.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_rasi(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "rasi not found"}), 404

    return jsonify({
        "id": user.id,
        "rasiname": user.rasiname,
        "notes": user.notes
    })


# UPDATE
def update_rasi(id):
    data = request.json

    user = User.query.get(id)

    if not user:
        return jsonify({"message": "rasi not found"}), 404

    user.rasiname = data["rasiname"]
    user.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "rasi updated successfully"})


# DELETE
def delete_rasi(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "rasi not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "rasi deleted successfully"})