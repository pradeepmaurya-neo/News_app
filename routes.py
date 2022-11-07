from flask import Blueprint, redirect, request
from models import User, Admin
from werkzeug.security import generate_password_hash

bp = Blueprint('routes', __name__)


@bp.route('/home')
def home():
    data = request.args
    print(data['name'],
        data['username'],
        generate_password_hash(data['password']),
        data['email'])
    user = User(name = data['name'],
        username=data['username'],
        password=generate_password_hash(data['password']),
        email = data['email']
        )
    return data['name'],data['username'], generate_password_hash(data['password']),data['email']