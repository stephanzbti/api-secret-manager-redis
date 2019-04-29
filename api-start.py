from flask import Flask, request
from flask_restful import Resource, Api
from src.controller.secret.getsecret import GetSecret as GetSecret
from src.controller.secret.removeAll import RemoveAll as RemoveAll
from src.controller.secret.remove import Remove as Remove
from decouple import config

PORT = config('PORT', '3000')
app = Flask(__name__)
api = Api(app)

api.add_resource(GetSecret, '/getsecret')  # Route 1
api.add_resource(RemoveAll, '/removeall')  # Route 0
api.add_resource(Remove, '/remove')  # Route 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
