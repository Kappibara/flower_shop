from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_restful import Api
from flask_jwt_extended import JWTManager
from authlib.flask.client import OAuth

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
api = Api(app)

jwt = JWTManager(app)
oauth = OAuth(app)
oauth.register(name='google')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
# csrf = CSRFProtect()
# csrf.init_app(app)
from api import routes
from api import controllers
