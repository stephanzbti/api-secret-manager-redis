from flask import Flask, request
from flask_restful import Resource, Api
import src.controller.secret.getsecret as GetSecret
import src.controller.secret.removeAll as RemoveAll
import src.controller.secret.remove as Remove
from decouple import config

PORT = config('PORT', '3000')
app = Flask(__name__)
api = Api(app)

api.add_resource(GetSecret, '/getsecret')  # Route 1
api.add_resource(RemoveAll, '/removeall')  # Route 0
api.add_resource(Remove, '/remove')  # Route 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
