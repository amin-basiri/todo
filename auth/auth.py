from flask import request
from flask import Blueprint
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from extensions import db
from models.auth import sign_up_schema, sign_in_schema, User


bp = Blueprint("auth", __name__, url_prefix='/auth')


@bp.route("/sign_up", methods=["POST"])
def sign_up():
    try:
        user = sign_up_schema.load(request.form)
    except ValidationError as e:
        return e.messages, 400

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return {"msg": "Username already used"}, 409

    return sign_up_schema.dump(user), 201


@bp.route("/sign_in", methods=['POST'])
def sign_in():
    try:
        data = sign_in_schema.load(request.form)
    except ValidationError as e:
        return e.messages, 400

    user = User.query.filter_by(username=data['username']).first()
    if user and user.is_password_ok(data['password']):
        return {"access_token": create_access_token(identity=data['username'])}
    return {"msg": "Sign in failed"}, 401
