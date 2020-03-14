from flask import request
from werkzeug.exceptions import BadRequest
from simple_chat.api.controllers import helper
from simple_chat.db.models import Users
from simple_chat.database import sql_db as db


class User:
    model = Users

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


