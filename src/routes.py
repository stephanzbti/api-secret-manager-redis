from src.controller.secret.getsecret import GetSecret as GetSecret
from src.controller.secret.removeAll import RemoveAll as RemoveAll
from src.controller.secret.remove import Remove as Remove
from flask_restful import Api

def routes(app):
    api = Api(app)

    api.add_resource(GetSecret, '/getsecret')  # Route 1
    api.add_resource(RemoveAll, '/removeall')  # Route 0
    api.add_resource(Remove, '/remove')  # Route 0