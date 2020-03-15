from sqlalchemy.ext.hybrid import hybrid_property

from simple_chat.database import sql_db as db
from simple_chat.db.models.base_model import BaseModel


class MessageLikes(BaseModel):
    # Properties
    # None

    # Foreign keys
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # N:1
    # users = db.relationship("Users", back_populates="likes", foreign_keys=user_id)

    # 1:N
    # None

    # 1:1
    # None

    __tablename__ = 'messages'

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @hybrid_property
    def user_name(self):
        if self.users:
            return [user.name for user in self.users]

        return ''
