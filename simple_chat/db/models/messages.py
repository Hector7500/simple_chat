from typing import List

from sqlalchemy import Index
from sqlalchemy.ext.hybrid import hybrid_property

from simple_chat.database import sql_db as db
from simple_chat.db.models.base_models import UUIDBaseModel


class Messages(UUIDBaseModel):
    # Properties
    message = db.Column(db.Text)

    # Foreign keys
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # N:1
    user = db.relationship("Users", back_populates="messages", foreign_keys=user_id)
    room = db.relationship("Rooms", back_populates="messages", foreign_keys=room_id)

    # 1:N
    likes = db.relationship("MessageLikes", back_populates="messages")

    # 1:1
    # None

    # Indexes
    message_index = Index('message_index', 'uuid')

    __tablename__ = 'messages'
    __table_args__ = (message_index,)

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @hybrid_property
    def uuid_str(self) -> str:
        return str(self.uuid)

    @hybrid_property
    def like_list(self) -> List:

        if self.likes:
            likes: List = []

            for like in self.likes:
                likes.append({
                    "user_name": like.users.name,
                    "user_uuid": like.users.uuid_str
                })

            return likes

        return []
