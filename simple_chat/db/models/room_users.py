from simple_chat.database import sql_db as db
from simple_chat.db.models.base_model import BaseModel


class RoomUsers(BaseModel):
    # Properties
    # None

    # Foreign keys
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # N:1
    # None

    # 1:N
    # None

    # 1:1
    # None

    __tablename__ = 'room_users'

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
