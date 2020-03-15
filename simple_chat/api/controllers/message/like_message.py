from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper, util as controller_util
from simple_chat.database import sql_db as db
from simple_chat.db.models import MessageLikes


class LikeMessage(Resource):
    def post(self):
        """
            POST endpoint for liking a message
            ---
            description: Like a user's message in the room
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
                  message_uuid:
                    type: string
                    description: room's uuid passed in the request body
            responses:
              201:
                description: User liked the message
        """
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing ids')

            return helper.create_no_json_response()

        user_id = controller_util.get_user_id(json_data['user_uuid'])
        message_id = controller_util.get_message_id(json_data['message_uuid'])

        new_like = MessageLikes(message_id=message_id, user_id=user_id)

        db.session.add(new_like)
        db.session.commit()

        msg = {
            'message': f'User successfully liked message',
            'user_uuid': json_data["user_uuid"],
            'message_uuid': json_data["message_uuid"]
        }

        return helper.successful_post_response(msg)
