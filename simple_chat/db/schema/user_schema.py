from marshmallow import fields

from simple_chat.db.schema.base_schema import BaseSchema


class UserSchema(BaseSchema):
    name = fields.Str()
