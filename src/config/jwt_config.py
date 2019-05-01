from flask_jwt_simple import JWTManager
from flask import jsonify
from src.utils.messages import MSG_INVALID_CREDENTIALS, MSG_TOKEN_EXPIRED, MSG_PERMISSION_DENIED

def configure_jwt(app):
    jwt = JWTManager(app)
    
    @jwt.jwt_data_loader
    def add_claims_to_access_token(identity):
        return {

        }

    @jwt.expired_token_loader
    def expired_token_callback():
        resp = jsonify({
            'status': 401,
            'sub_status': 42,
            'message': MSG_TOKEN_EXPIRED
        })

        resp.status_code = 401

        return resp

    @jwt.unauthorized_loader
    def unauthorized_callback(e):
        resp = jsonify({
            'status': 401,
            'sub_status': 1,
            'description': e,
            'message': MSG_INVALID_CREDENTIALS
        })

        resp.status_code = 401

        return resp

    @jwt.invalid_token_loader
    def invalid_token_loader_callback(e):
        resp = jsonify({
            'status': 401,
            'sub_status': 3,
            'description': e,
            'message': MSG_INVALID_CREDENTIALS
        })

        resp.status_code = 401

        return resp
