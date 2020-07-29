from flask_restful import Api
from api import app
from api.controllers import MainHandler

api = Api(app)

api.add_resource(MainHandler, '/')
