from flask import request
from flask import Blueprint
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from extensions import db
from models.auth import sign_up_schema


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
        return {"msg": "Username already used"}, 400

    return sign_up_schema.dump(user)
