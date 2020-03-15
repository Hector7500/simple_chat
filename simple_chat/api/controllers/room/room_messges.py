from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Rooms


class RoomMessages(Resource):
    def get(self):
        """
            GET endpoint for room data
            ---
            description: Get all messages and likes associated with the message
            parameters:
              - name: room_uuid
                in: path
                type: string
                required: true
                description: used as query param
            definitions:
              User:
                type: object
                properties:
                  user:
                    name: string
            responses:
              201:
                description: Get all messages and likes associated with the message in list
        """


        try:
            room_uuid = request.args['room_uuid']

        except BadRequest:

            return helper.create_missing_fields_response('room_uuid')

        room = db.session.query(Rooms).filter(Rooms.uuid == room_uuid).first()

        room_data = {
            'users': room.user_list,
            'messages': room.message_list
        }

        return helper.response(room_data, 200)
