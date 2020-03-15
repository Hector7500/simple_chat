from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper
from simple_chat.database import sql_db as db
from simple_chat.db.models import Users


class User(Resource):
    def post(self):
        """
            POST endpoint for creating new users
            ---
            description: POST endpoint for creating new users
            parameters:
              - name: name
                in: path
                type: string
                required: true
                description: Used in request body
            definitions:
              User:
                type: object
                properties:
                  user:
                    name: string
            responses:
              201:
                description: Creates a new user
        """
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
        """
            GET endpoint for getting details of user
            ---
            description: GET endpoint for getting details of user
            parameters:
              - name: user_id
                in: path
                type: int
                required: true
                description: Used as query param
            definitions:
              User:
                type: object
                properties:
                  user:
                    name: string
            responses:
              201:
                description: Creates a new user
        """
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
