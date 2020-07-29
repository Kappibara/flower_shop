from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
api = Api(app)

jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
# csrf = CSRFProtect()
# csrf.init_app(app)
from api.models import *
from api.controllers import *
from api.controllers import MainHandler, LoginHandler, RegistrationHandler

api.add_resource(MainHandler, '/')
api.add_resource(LoginHandler, '/login')
api.add_resource(RegistrationHandler, '/registration')


