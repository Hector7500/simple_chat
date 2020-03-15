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
    # None

    # 1:N
    # None

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
    def rooms_list(self):
        if self.rooms:
            return [room.name for room in self.rooms]

        return ''
