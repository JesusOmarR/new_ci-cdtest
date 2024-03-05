from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TaskModel
from schemas.users import TaskSchema

blp = Blueprint("Tasks", __name__, description="Tasks operation")


@blp.route("/task")
class Tasks(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.query.all()

    @blp.arguments(TaskSchema)
    def post(self, task_data):
        task = TaskModel(**task_data)
        try:
            db.session.add(task)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="ps")

        return task


@blp.route("/task/<string:task_id>")
class Tasks(MethodView):
    def get(self):
        pass
