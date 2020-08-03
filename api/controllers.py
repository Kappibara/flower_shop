from flask import request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flask_restful import Resource

from api import db
from api.models import Products, Users
from api.utils import is_int, serialize_product


class MainHandler(Resource):

    def get(self):
        products = Products.query.filter(Products.id > 0).order_by(Products.id).limit(3).with_entities(
            Products.id, Products.image_url, Products.description).all()
        result = {}
        for product in products:
            result[product[0]] = {"image_url": product[1], "description": product[2]}
        return result

    @jwt_required
    def post(self):
        user = get_jwt_identity()
        return {'hello': "My friend, {}".format(user)}


class LoginHandler(Resource):
    def post(self):
        data = request.get_json()
        user = Users.query.filter(Users.username == data.get("username", "")).first_or_404()
        if user and user.verify_password(data.get("password", "")):
            access_token = create_access_token(identity=user.username)
            return {"token": access_token}
        return {"error": "wrong credentials"}

    def get(self):
        user = Users(username='test', gender="MALE", phone="1231", email="test@gmail.com", password="test", role="ADMIN")
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            return {"error": "Not unique"}
        return {"result": "SUCCESS"}


class RegistrationHandler(Resource):
    def post(self):
        """required:
            :param username: str
            :param password: str
            :param gender: str
            :param email: str
            :param phone: str
        """
        data = request.get_json()
        try:
            user = Users(**data)
        except Exception as e:
            return {"error": "Wrong data", "message": e}
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            # TODO сделать разные обработки ошибок
            return {"error": "Not unique"}
        token = create_access_token(identity=user.username)
        return {"token": token}


class Favourites(Resource):

    @jwt_required
    def post(self):
        data = request.get_json()
        username = get_jwt_identity()
        print(username)
        u = Users.query.filter(Users.username == username).scalar()
        print(u)
        print(u)
        print(u)
        print(u.favourite)
        # if u.favourite is None:

        # u.favourite = u.favourite.append(data['favourite_id'])
        u.favourite = [1]
        db.session.add(u)
        db.session.commit()
        return {}

    def get(self):
        # username = get_jwt_identity()
        pass




class GetProducts(Resource):

    def get(self):
        data = request.get_json()
        if is_int(data):
            products = Products.query.offset(data['offset']).limit(data['limit'])
            return {'products': [serialize_product(p) for p in products]}
        return {
            "errors": "offset and limit must be integer",
            "code": 401
        }


