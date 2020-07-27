from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from api import db, app
from sqlalchemy.dialects.postgresql import UUID

import uuid


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_url = db.Column(db.String(255))
    price = db.Column(db.DECIMAL)
    title = db.Column(db.String(255))
    description = db.Computed(db.Text, default="")
    ingredients = db.Column(db.Integer, )
    id_category = db.Column()


class Payment(db.Model):
    payment_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_price = db.Column(db.DECIMAL)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    payment_method = db.Column(db.Integer)
    comments = db.Column(db.Text)
    user_name = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(100))


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

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
