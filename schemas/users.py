from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)


class PlainTaskSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    done = fields.Boolean(required=True)
    user_id = fields.Str(required=True)


class UserSchema(PlainUserSchema):
    tasks = fields.List(fields.Nested(PlainTaskSchema()), dump_only=True)


class TaskSchema(PlainTaskSchema):
    user_id = fields.Int(required=True, load_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
