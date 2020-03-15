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
    # None

    # 1:N
    # None

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
    def users_list(self):
        if self.users:
            return [user.name for user in self.users]

        return ''
