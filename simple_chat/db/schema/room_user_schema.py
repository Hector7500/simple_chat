from marshmallow import fields

from simple_chat.db.schema.base_schema import BaseSchema


class RoomUserSchema(BaseSchema):
    room_id = fields.Integer()
    user_id = fields.Integer()
