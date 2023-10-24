from marshmallow import ValidationError
from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from extensions import db
from models.todo import add_todo_schema


bp = Blueprint("todo", __name__, url_prefix='/todo')


@bp.route("/", methods=["POST"])
@jwt_required()
def add_todo():
    try:
        todo = add_todo_schema.load(data={**request.form, "user_id": get_jwt_identity()})
    except ValidationError as e:
        return jsonify(e.messages), 400

    db.session.add(todo)
    db.session.commit()

    return add_todo_schema.dump(todo), 201
