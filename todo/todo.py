import datetime

from marshmallow import ValidationError
from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from extensions import db
from models.todo import add_todo_schema, edit_todo_schema, Todo


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


@bp.route("/<int:todo_id>", methods=["PUT"])
@jwt_required()
def edit_todo(todo_id: int):

    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return jsonify(msg="Todo not found"), 404

    try:
        todo = edit_todo_schema.load(
            request.form, instance=todo, partial=True
        )
    except ValidationError as e:
        return jsonify(e.messages), 400

    db.session.commit()

    return edit_todo_schema.dump(todo), 202


@bp.route("/<int:todo_id>", methods=["DELETE"])
@jwt_required()
def delete_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return jsonify(msg="Todo not found"), 404

    todo.deleted = datetime.datetime.utcnow()
    db.session.commit()

    return jsonify(msg="Successfully deleted"), 202
