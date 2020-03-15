from typing import Any, Dict

from flask import jsonify


def create_no_json_response():
    msg = 'No parameters provided. Add json body.'
    data = {'status': 400, 'message': msg}

    return response(data, 400)


def successful_post_response(data_dict: Dict) -> Any:

    data_dict['status'] = 201

    return response(data_dict, 201)


def create_missing_fields_response(param_str):
    msg = f'Missing parameters: {param_str}'
    data = {'status': 400, 'message': msg}

    return response(data, 400)


def response(data: Any, code: int) -> Any:
    response_data = jsonify(data)
    response_data.status_code = code

    return response_data
