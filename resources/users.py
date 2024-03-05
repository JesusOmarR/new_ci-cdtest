from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from schemas.users import PlainUserSchema, UserSchema

blp = Blueprint("users", __name__, description="Users operation")
from db import db
from models import UserModel


@blp.route("/users")
class Users(MethodView):
    
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error has ocurred")

        return user


@blp.route("/users/<string:user_id>")
class Users(MethodView):
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)


