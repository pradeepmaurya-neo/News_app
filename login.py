from flask import Blueprint, request, redirect, jsonify
from werkzeug.security import check_password_hash
from models import User
from db import session

login_bp = Blueprint('login', __name__)


@login_bp.route('/login')
def login():
    data = request.form
    passw = session.query(User).filter(User.username==data['username']).first()
    try:
        if check_password_hash(passw.password, data['password']):
            print("You are authorize for login")
        else:
            return jsonify({
        "status": "failed",
        "meassage" : "Login Failed please try again"
    })
    except Exception as e:
        print(e)
    return jsonify({
        "status": "success",
        "meassage" : passw.name
    })
