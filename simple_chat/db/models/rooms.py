from simple_chat.database import sql_db as db
from simple_chat.db.models.base_model import BaseModel


class Rooms(BaseModel):
    # ============
    # Properties ===
    # ============
    name = db.Column(db.String)

    # Foreign keys
    # None

    # N:1
    # None

    # 1:N
    # None

    # 1:1
    # None

    __tablename__ = 'rooms'

    # =========
    # Methods ===
    # =========
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
