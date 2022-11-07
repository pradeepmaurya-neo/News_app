from flask import Blueprint, redirect, request
from models import User, Admin
from werkzeug.security import generate_password_hash
from db import session

bp = Blueprint('routes', __name__)


@bp.route('/home', methods=['GET'])
def home():
    data = request.form
    
    print(data['email'])
    print(data['name'],data['username'], generate_password_hash(data['password']),data['email'])
    user = User(name = data['name'],
        username=data['username'],
        password=generate_password_hash(data['password']),
        email = data['email']
        )
    session.add(user)
    session.commit()
    return "data['name'],data['username'], generate_password_hash(data['password']),data['email']"
    # return "success"


@bp.route('/admin', methods=['GET'])
def admin():
    data = request.form
    data1 = dict(name = data['name'],
        username=data['username'],
        password=generate_password_hash(data['password']))
    user = Admin(**data1)
    session.add(user)
    session.commit()
    return data1