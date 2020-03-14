from flask import request
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Rooms


class Room:
    def post(self):
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing name or description')

            return helper.create_no_json_response()

        new_room = Rooms(name=json_data['name'])

        db.session.add(new_room)
        db.session.commit()

        return helper.successful_post_response('room')

    def get(self):
        rooms = db.session.query(Rooms).all()
        rooms_data = [{
            'name': room.name,
            'rooms': room.users_list,
            'status': 200
        } for room in rooms]

        return helper.response(rooms_data, 200)
