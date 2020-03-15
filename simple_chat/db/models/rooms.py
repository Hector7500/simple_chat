from typing import List

from sqlalchemy import Index
from sqlalchemy.ext.hybrid import hybrid_property

from simple_chat.database import sql_db as db
from simple_chat.db.models.base_models import UUIDBaseModel


class Rooms(UUIDBaseModel):
    # Properties
    name = db.Column(db.String)

    # Foreign keys
    # None

    # N:1
    users = db.relationship("RoomUsers", back_populates="room")

    # 1:N
    messages = db.relationship("Messages", back_populates="room")

    # 1:1
    # None

    # Indexes
    room_index = Index('room_index', 'uuid')

    __tablename__ = 'rooms'
    __table_args__ = (room_index,)

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @hybrid_property
    def uuid_str(self) -> str:
        return str(self.uuid)

    @hybrid_property
    def user_list(self) -> List:
        if self.users:
            users_list: List = []

            for user_room in self.users:
                users_list.append({
                    "name": user_room.user.name,
                    "user_uuid": user_room.user.uuid_str,
                })

            return users_list

        return []

    @hybrid_property
    def message_list(self) -> List:
        if self.messages:
            message_list: List = []
            for message in self.messages:
                message_list.append(
                    {
                        "message": message.message,
                        "user_uuid": message.user.uuid_str,
                        "user_name": message.user.name,
                        "likes": message.like_list
                    })
            return message_list

        return []
