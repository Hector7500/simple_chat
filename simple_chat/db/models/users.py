from typing import List

from sqlalchemy import Index
from sqlalchemy.ext.hybrid import hybrid_property

from simple_chat.database import sql_db as db
from simple_chat.db.models.base_models import UUIDBaseModel


class Users(UUIDBaseModel):
    # Properties
    name = db.Column(db.String)

    # Foreign keys
    # None

    # N:1
    rooms = db.relationship("RoomUsers", back_populates="user")
    messages = db.relationship("Messages", back_populates="user")

    # 1:N
    likes = db.relationship("MessageLikes", back_populates="users")

    # 1:1
    # None

    # Indexes
    user_index = Index('user_index', 'uuid')

    __tablename__ = 'users'
    __table_args__ = (user_index,)

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @hybrid_property
    def uuid_str(self) -> str:
        return str(self.uuid)

    @hybrid_property
    def rooms_list(self) -> List:
        if self.rooms:
            room_list: List = []
            for room in self.rooms:
                room_list.append({
                    "name": room.name,
                    "uuid": room.uuid_str
                })

            return room_list

        return []
