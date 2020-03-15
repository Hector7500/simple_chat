from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

from simple_chat.database import sql_db as db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    __abstract__ = True


class UUIDBaseModel(BaseModel, db.Model):
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False, server_default=text("uuid_generate_v4()"))

    __abstract__ = True
