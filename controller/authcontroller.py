from flask import request, jsonify
from model.authmodel import User
from database import db


def register_user():
    data = request.json

    user = User(
        username=data["username"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"})


def login_user():
    data = request.json

    user = User.query.filter_by(username=data["username"]).first()

    if user and user.password == data["password"]:
        return jsonify({"message": "Login successful"})
    
    return jsonify({"message": "Invalid credentials"}), 401