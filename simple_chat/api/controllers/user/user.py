from flask import request
from werkzeug.exceptions import BadRequest
from simple_chat.api.controllers import helper
from simple_chat.db.models import Users
from simple_chat.database import sql_db as db


class User:
    def post(self):
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing name or description')

            return helper.create_no_json_response()

        new_user = Users(name=json_data['name'])

        db.session.add(new_user)
        db.session.commit()

        return helper.successful_post_response('user')

    def get(self):
        try:
            user_id = int(request.args['user_id'])

        except Exception:

            return helper.create_missing_fields_response('user_id')

        user = db.session.query(Users).filter(Users.id == user_id).first()
        user_data = {
            'name': user.name,
            'rooms': user.rooms_list,
            'status': 200
        }

        return helper.response(user_data, 200)





