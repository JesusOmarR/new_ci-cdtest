from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    done = db.Column(db.Boolean)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
    )
    user = db.relationship("UserModel", back_populates="tasks")
