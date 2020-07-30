from api import api
from api.controllers import (
    MainHandler, LoginHandler, RegistrationHandler
)

api.add_resource(MainHandler, '/')
api.add_resource(LoginHandler, '/login')
api.add_resource(RegistrationHandler, '/registration')
