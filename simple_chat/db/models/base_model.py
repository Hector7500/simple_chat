from sqlalchemy import func

from simple_chat.database import sql_db as db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    __abstract__ = True
