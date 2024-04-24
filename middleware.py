import jwt
from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, 'secret')
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(data['id'], *args, **kwargs)

    return decorated
