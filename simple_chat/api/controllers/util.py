from simple_chat.database import sql_db as db
from simple_chat.db.models import Messages, Rooms, Users


def get_user_id(user_uuid: str) -> int:
    user_id = db.session.query(Users.id).filter(Users.uuid == user_uuid).scalar()

    return user_id


def get_room_id(room_uuid: str) -> int:
    room_id = db.session.query(Rooms.id).filter(Rooms.uuid == room_uuid).scalar()

    return room_id


def get_message_id(message_uuid: str) -> int:
    message_id = db.session.query(Messages.id).filter(Messages.uuid == message_uuid).scalar()

    return message_id
