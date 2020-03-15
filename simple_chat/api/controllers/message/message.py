from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Messages
from simple_chat.api.controllers import util as controller_util


class Message(Resource):
    def post(self):
        """
            POST endpoint for room messages
            ---
            description: Post a new message to the room
            parameters:
              - name: room_uuid
                in: path
                type: string
                required: true
                description: room's uuid passed in the request body
              - name: user_uuid
                in: path
                type: string
                required: true
                description: user's uuid passed in the request body
            definitions:
              User:
                type: object
                properties:
                  user:
                    name: string
            responses:
              201:
                description: Created new message in the room
        """
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing message or ids')

            return helper.create_no_json_response()

        user_id = controller_util.get_user_id(json_data['user_uuid'])
        room_id = controller_util.get_room_id(json_data['room_uuid'])

        new_message = Messages(message=json_data['message'], user_id=user_id, room_id=room_id)
        db.session.add(new_message)
        db.session.commit()

        msg = f'User {json_data["user_uuid"]} successfully sent message to room {json_data["room_uuid"]}'

        return helper.successful_post_response(msg)

