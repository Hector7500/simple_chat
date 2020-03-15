from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Rooms


class CreateRoom(Resource):
    def post(self):
        """
            POST endpoint for room messages
            ---
            description: Post a new message to the room
            parameters:
              - name: name
                in: path
                type: string
                required: true
                description: room's name passed in the request body
            definitions:
              User:
                type: object
                properties:
                  user:
                    type: string
            responses:
              201:
                description: Created new room returns UUID
        """
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing name')

            return helper.create_no_json_response()

        new_room = Rooms(name=json_data['name'])

        db.session.add(new_room)
        db.session.commit()

        return helper.successful_post_response(f'Successfully created room {new_room.uuid}')


