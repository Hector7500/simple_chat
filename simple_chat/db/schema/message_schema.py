from marshmallow import fields

from simple_chat.db.schema.base_schema import BaseSchema


class MessageSchema(BaseSchema):
    message = fields.String()
    uuid = fields.UUID()
    room_id = fields.Integer()
    user_id = fields.Integer()
