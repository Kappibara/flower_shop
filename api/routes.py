from flask_restful import Api
from api import app, HelloWorld

api = Api(app)

api.add_resource(HelloWorld, '/')
