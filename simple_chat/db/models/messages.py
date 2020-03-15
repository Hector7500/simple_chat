from sqlalchemy import Index

from simple_chat.database import sql_db as db
from simple_chat.db.models.base_models import UUIDBaseModel


class Messages(UUIDBaseModel):
    # Properties
    message = db.Column(db.Text)

    # Foreign keys
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # N:1
    # None

    # 1:N
    # None

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
