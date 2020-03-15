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
            description: create a new user
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
                    type: string
            responses:
              201:
                description: Creates a new user returns UUID
        """
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing name')

            return helper.create_no_json_response()

        new_user = Users(name=json_data['name'])

        db.session.add(new_user)
        db.session.commit()

        msg = {
            'message': f'User successfully created',
            'user_uuid': new_user.uuid
        }

        return helper.successful_post_response(msg)

    def get(self):
        """
            GET endpoint for all rooms
            ---
            description: Get all rooms
            definitions:
              Room:
                type: object
                properties:
                  room_name:
                    type: string
                    description: name of room
                  room_uuid:
                    type: string
                    description: room uuid
            responses:
              201:
                description: Get all rooms ie. name and uuid
        """

        users = db.session.query(Users).all()

        users_data = [{
            'user_name': user.name,
            'user_uuid': user.uuid_str
        } for user in users]

        return helper.response(users_data, 201)
