from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper, util as controller_util
from simple_chat.database import sql_db as db
from simple_chat.db.models import RoomUsers


class JoinRoom(Resource):
    def post(self):
        """
            POST endpoint for joining room
            ---
            description: Join room
            definitions:
              Room:
                type: object
                properties:
                  user_uuid:
                    type: string
                    description: user's uuid passed in the request body
                  room_uuid:
                    type: string
                    description: room's uuid passed in the request body
            responses:
              201:
                description: User joined the room
        """
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing ids')

            return helper.create_no_json_response()

        user_id = controller_util.get_user_id(json_data['user_uuid'])
        room_id = controller_util.get_room_id(json_data['room_uuid'])

        new_user_in_room = RoomUsers(user_id=user_id, room_id=room_id)

        db.session.add(new_user_in_room)
        db.session.commit()

        return helper.successful_post_response(f'User {json_data["user_uuid"]} successfully joined room '
                                               f'{json_data["room_uuid"]}')
