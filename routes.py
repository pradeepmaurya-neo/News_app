from flask import Blueprint, redirect, request, jsonify
from models import User, Admin
from werkzeug.security import generate_password_hash
from db import session

bp = Blueprint('routes', __name__)


@bp.route('/user/add', methods=['GET'])
def add_user():
    data = request.form
    
    print(data['email'])
    print(data['name'],data['username'], generate_password_hash(data['password']),data['email'])
    user = User(name = data['name'],
        username=data['username'],
        password=generate_password_hash(data['password']),
        email = data['email'],
        admin_id = data['admin_id']
        )
    session.add(user)
    session.commit()
    return jsonify({
        "status": "success",
        "meassage" : data
    })


@bp.route('/add/admin', methods=['GET'])
def add_admin():
    data = request.form
    data1 = dict(name = data['name'],)
    user = Admin(**data1)
    session.add(user)
    session.commit()
    return jsonify({
        "status": "success",
        "meassage" : data1
    })