from random import randint

from sqlalchemy.exc import IntegrityError
from faker import Faker
from api import db, manager
from api.models import Users, Role, Products, Categories


u = Users.query.filter(Users.id==11).first()
u.favourites = []

@manager.command
def create_users():
    fake = Faker()
    for _ in range(10):
        print(1)
        u = Users(email=fake.email(),username=fake.user_name(),password='password',gender='MALE',role=Role.USER.name,addresses=[{"address": "my city"}], phone=fake.phone_number())
        db.session.add(u)
        try:
            print(2)
            db.session.commit()
            print(4)
        except IntegrityError:
            print(3)
            db.session.rollback()


@manager.command
def create_products(count=50):
    fake = Faker()
    i = 0
    while i < count:
        print(1)
        p = Products(
            image_url="https://4.bp.blogspot.com/-FKE9GFijdz0/Tej5mFItFhI/AAAAAAAAAYk/68jAt6ZskPw/s1600/P5152937%25D1%2580.jpg",
            price=randint(1000, 5000),
            title=fake.text(),
            description=fake.text(),
        )
        db.session.add(p)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


@manager.command
def create_categories(count=50):
    fake = Faker()
    i = 1
    while i < count:
        print(1)
        p = Products.query.filter(Products.id==i).first()
        c = Categories(
            name=fake.user_name(),
        )
        p.categories.append(c)
        db.session.add(c)
        db.session.add(p)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


if __name__ == '__main__':
    # create_users()
    # create_products()
    create_categories()