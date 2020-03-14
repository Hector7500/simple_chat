from typing import Any

from flask import jsonify


def create_no_json_response():
    msg = 'No parameters provided. Add json body.'
    data = {'status': 400, 'message': msg}
    return response(data, 400)


def successful_post_response(data_type: str) -> Any:
    msg = f'Succesfully Created {data_type}'
    data = {'status': 201, 'message': msg}

    return response(data, 201)


def response(data: Any, code: int) -> Any:
    response = jsonify(data)
    response.status_code = code
    return response
