from flask import Flask
from flask_cors import CORS

from simple_chat.database import sql_db, marsh
from simple_chat import util

flask_app = Flask(__name__)
CORS(flask_app, supports_credentials=True)
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['SQLALCHEMY_ECHO'] = False
flask_app.config['SQLALCHEMY_DATABASE_URI'] = util.get_db_str()
flask_app.config['MAX_CONTENT_LENGTH'] = 80000 * 1024 * 1024
sql_db.init_app(flask_app)
marsh.init_app(flask_app)


@flask_app.route('/')
def root():
    return 'Flask app up and running'
