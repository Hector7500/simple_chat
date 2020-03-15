from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Messages, Rooms


class RoomMessages(Resource):
    def post(self):
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing name or description')

            return helper.create_no_json_response()

        new_message = Messages(message=json_data['message'], user_id=json_data['user_id'], room_id=['room_id'])

        db.session.add(new_message)
        db.session.commit()

        return helper.successful_post_response('room')

    def get(self):
        try:
            room_id = int(request.args['room_id'])

        except Exception:

            return helper.create_missing_fields_response('room_id')

        room = db.session.query(Rooms).filter(Rooms.id == room_id)
        room_data = [
            {
                'message': data.message_data,
                'likes': data.like_data,

            } for data in room]

        return helper.response(room_data, 200)
