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
from api import routes
from api import controllers
