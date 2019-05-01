from flask import Flask, request
from src.config.jwt_config import configure_jwt
from src.routes import routes
from decouple import config

PORT = config('PORT', '3000')

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = config('JWT_SECRET', '')
app.config['PROPAGATE_EXCEPTIONS'] = True

configure_jwt(app)
routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
