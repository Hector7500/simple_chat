from sqlalchemy.ext.hybrid import hybrid_property

from simple_chat.database import sql_db as db
from simple_chat.db.models.base_models import BaseModel


class MessageLikes(BaseModel):
    # Properties
    # None

    # Foreign keys
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # N:1
    users = db.relationship("Users", back_populates="likes", foreign_keys=user_id)
    messages = db.relationship("Messages", back_populates="likes", foreign_keys=message_id)

    # 1:N
    # None

    # 1:1
    # None

    # Indexes
    # None

    __tablename__ = 'messages_likes'

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)