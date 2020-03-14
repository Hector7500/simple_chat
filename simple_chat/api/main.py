import os

from flask import Blueprint, jsonify
from flask_restful import Api

from simple_chat.api.controllers.user.user import User

dir_path = os.path.dirname(os.path.realpath(__file__))

version_value = os.environ['APP_VERSION'].replace('.', '_')
version_name = 'v' + version_value

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
                  default: 0_12_0
        """
    return jsonify({'version': version_value})

restful_api = Api(app_v0_1_0)

restful_api.add_resource(User, f'/users', endpoint='users')



restful_api.init_app(app_v0_1_0)