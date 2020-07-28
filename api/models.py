from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from api import db, app
from sqlalchemy.dialects.postgresql import UUID

import uuid
import enum

product_category = db.Table(
    'product_category',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

product_flower = db.Table(
    'product_flower',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('flower_id', db.Integer, db.ForeignKey('flower.id'), primary_key=True)
)


class Role(enum.Enum):
    ADMIN = 0
    USER = 1


class PaymentMethod(enum.Enum):
    CASH = 0
    LIQPAY = 1
    APPLEPAY = 2


class Gender(enum.Enum):
    MALE = 0
    FEMALE = 1


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    price = db.Column(db.DECIMAL)
    title = db.Column(db.String(255))
    description = db.Column(db.Text, default='')
    ingredients = db.relationship('Flower', secondary=product_flower, lazy='subquery',
                                  backref=db.backref('product', lazy=True))
    categories = db.relationship('Category', secondary=product_category, lazy='subquery',
                                 backref=db.backref('products', lazy=True))


class UserAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(100))
    street = db.Column(db.String(200))
    house = db.Column(db.Integer)
    flat = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Order(db.Model):
    order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_price = db.Column(db.DECIMAL)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    payment_method = db.Column(db.Enum(PaymentMethod))
    comment = db.Column(db.Text)
    user_name = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(Gender))
    phone = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    addresses = db.relationship('UserAddresses', back_populates='user')
    orders = db.relation('Order', backref='user', lazy=True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # role = db.Column('Role', back_populates='users')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def __repr__(self):
        return (f'<User id: {self.id},'
                f'username: {self.username},'
                f'email: {self.email}>')


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    sub_title = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class Metadata(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    call_center_phone = db.Column(db.String(20))
    locations = db.Column(db.ARRAY(db.String))


# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(120), unique=True, nullable=False)
#     users = db.relationship("User", back_populates='role')