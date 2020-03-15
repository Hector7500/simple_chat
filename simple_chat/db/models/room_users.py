from simple_chat.database import sql_db as db
from simple_chat.db.models.base_models import BaseModel


class RoomUsers(BaseModel):
    # Properties
    # None

    # Foreign keys
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # 1:N
    user = db.relationship("Users", back_populates="rooms", foreign_keys=user_id)
    room = db.relationship("Rooms", back_populates="users", foreign_keys=room_id)

    # N:1
    # None

    # 1:1
    # None

    # Indexes
    # None

    __tablename__ = 'room_users'

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
