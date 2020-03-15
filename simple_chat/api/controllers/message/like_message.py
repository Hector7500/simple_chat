from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import MessageLikes


class LikeMessage(Resource):
    def post(self):
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing name or description')

            return helper.create_no_json_response()

        new_like = MessageLikes(message=json_data['message_id'], user_id=json_data['user_id'], room_id=['room_id'])

        db.session.add(new_like)
        db.session.commit()

        return helper.successful_post_response('room')
