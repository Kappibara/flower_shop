from api import api
from api.controllers import (
    MainHandler, LoginHandler, RegistrationHandler, Favourites
)

api.add_resource(MainHandler, '/')
api.add_resource(LoginHandler, '/login')
api.add_resource(RegistrationHandler, '/registration')
api.add_resource(Favourites, '/favourites')
