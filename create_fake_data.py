from sqlalchemy.exc import IntegrityError
from faker import Faker
from api import db, manager
from api.models import Product, User, Role


@manager.command
def run():
    fake = Faker()
    for _ in range(10):
        print(1)
        u = User(email=fake.email(),username=fake.user_name(),password='password',gender='MALE',role=Role.USER.name,addresses=[{"address": "my city"}], phone=fake.phone_number())
        db.session.add(u)
        try:
            print(2)
            db.session.commit()
            print(4)
        except IntegrityError:
            print(3)
            db.session.rollback()


manager.add_command("faker", Faker())

def product(count=100):
    fake = Faker()
    i = 0
    while i < count:
        print(1)
        p = Product(
            image_url=fake.text(),
            price=1000,
            title=fake.text(),
            description=fake.text(),
        )
        db.session.add(p)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()
