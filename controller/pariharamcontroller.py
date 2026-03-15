from flask import request, jsonify
from model.pariharammodel import Pariharam
from database import db


# CREATE
def add_pariharam():
    data = request.json

    pariharam = Pariharam(
        pariharamname=data["pariharamname"],
        notes=data["notes"]
    )

    db.session.add(pariharam)
    db.session.commit()

    return jsonify({"message": "pariharam added successfully"})


# GET ALL
def get_pariharam():
    pariharams = Pariharam.query.all()

    result = []

    for p in pariharams:
        result.append({
            "id": p.id,
            "pariharamname": p.pariharamname,
            "notes": p.notes
        })

    return jsonify(result)


# GET SINGLE
def get_single_pariharam(id):
    pariharam = Pariharam.query.get(id)

    if not pariharam:
        return jsonify({"message": "pariharam not found"}), 404

    return jsonify({
        "id": pariharam.id,
        "pariharamname": pariharam.pariharamname,
        "notes": pariharam.notes
    })


# UPDATE
def update_pariharam(id):
    data = request.json

    pariharam = Pariharam.query.get(id)

    if not pariharam:
        return jsonify({"message": "pariharam not found"}), 404

    pariharam.pariharamname = data["pariharamname"]
    pariharam.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "pariharam updated successfully"})


# DELETE
def delete_pariharam(id):
    pariharam = Pariharam.query.get(id)

    if not pariharam:
        return jsonify({"message": "pariharam not found"}), 404

    db.session.delete(pariharam)
    db.session.commit()

    return jsonify({"message": "pariharam deleted successfully"})