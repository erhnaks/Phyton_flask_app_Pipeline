from flask_testing import TestCase
from application import app, db
from application.models import Chef, Pizza
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app


    def setUp(self):
        db.create_all()

        chef1 = Chef(name="erhan")
        db.session.add(chef1)
        db.session.commit()

        pizza1 = Pizza(
        name="pizza", crust= "Deep", base= "Capsicum", topping1="Beef",
        topping2="Pepper mild", topping3="Onion", topping4="Pineapple", topping5="Capsicum")
        db.session.add(pizza1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class Testresponse(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'erhan',response.data)
        self.assertIn(b'pizza',response.data)
        self.assertIn(b'Deep',response.data)
        self.assertIn(b'Capsicum',response.data)
        self.assertIn(b'Beef',response.data)
        self.assertIn(b'Pepper mild',response.data)
        self.assertIn(b'Onion',response.data)
        self.assertIn(b'Pineapple',response.data)
        self.assertIn(b'Capsicum',response.data)