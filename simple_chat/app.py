from flask import Flask
from flask_cors import CORS

flask_app = Flask(__name__)
CORS(flask_app, supports_credentials=True)


@flask_app.route('/')
def root():
    return 'Flask app up and running'
