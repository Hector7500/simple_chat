from flask_restful import Resource

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Rooms


class RoomList(Resource):
    def get(self):
        """
            GET endpoint for all rooms
            ---
            description: Get all rooms
            definitions:
              Room:
                type: object
                properties:
                  room_name:
                    type: string
                    description: name of room
                  room_uuid:
                    type: string
                    description: room uuid
            responses:
              201:
                description: Get all rooms ie. name and uuid
        """

        rooms = db.session.query(Rooms).all()

        rooms_data = [{
            'room_name': room.name,
            'room_uuid': room.uuid_str,
            'room_users': room.user_list
        } for room in rooms]

        return helper.response(rooms_data, 201)
