import os

from flask import Blueprint, jsonify
from flask_restful import Api

from simple_chat.api.controllers.message.like_message import LikeMessage
from simple_chat.api.controllers.message.message import Message
from simple_chat.api.controllers.room.create_room import CreateRoom
from simple_chat.api.controllers.room.join_room import JoinRoom
from simple_chat.api.controllers.room.rooms import RoomList
from simple_chat.api.controllers.room.room_messges import RoomMessages
from simple_chat.api.controllers.user.user import User

dir_path = os.path.dirname(os.path.realpath(__file__))

version_value = os.environ['APP_VERSION'].replace('.', '_')
version_name = f'v{version_value}'

app_v0_1_0 = Blueprint(version_name, version_name)


# Web routes
@app_v0_1_0.route('/')
def version_hello():
    """
        Return the api version
        ---
        tags:
          - app
        responses:
          200:
            description: The API version
            schema:
              id: version
              properties:
                version:
                  type: string
                  default: 0_1_0
        """
    return jsonify({'version': version_value})


rest_api = Api(app_v0_1_0)

rest_api.add_resource(User, f'/users', endpoint='users')
rest_api.add_resource(CreateRoom, f'/create-room', endpoint='create-room')
rest_api.add_resource(JoinRoom, f'/join-room', endpoint='join-rooms')
rest_api.add_resource(RoomList, f'/rooms', endpoint='rooms')
rest_api.add_resource(RoomMessages, f'/messages', endpoint='messages')
rest_api.add_resource(Message, f'/message', endpoint='message')
rest_api.add_resource(LikeMessage, f'/like-message', endpoint='message-likes')

rest_api.init_app(app_v0_1_0)
