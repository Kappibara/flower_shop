from flask_restful import Resource, Api

from api import app
from api.admin.blueprint import adminka

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world11111'}


api.add_resource(HelloWorld, '/')
app.register_blueprint(adminka, url_prefix='/adminka')


