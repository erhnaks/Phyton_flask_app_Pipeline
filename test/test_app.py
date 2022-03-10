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


    def test_chefform_get(self):
        response = self.client.get(url_for('createchef'))
        self.assertEqual(response.status_code, 200)
    
    def test_pizzaform_get(self):
        response = self.client.get(url_for('createpizza'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('updatechef', name=("erhan")))
        self.assertEqual(response.status_code, 200)

# Testing the CRUD Functionality on Chef Model

class TestCRUDChef(TestBase):

    def test_read_chef(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'erhan', response.data)
    
    def test_create_chef(self):
        response = self.client.post(url_for('createchef'),
        data=dict(name="Harry"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Harry', response.data)

    def test_update_chef(self):
        response = self.client.post(url_for("updatechef", name="erhan"),
        data=dict(name="updated"),
        follow_redirects=True
    )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'updated', response.data)


    def test_delete_chef(self):
        response = self.client.post(url_for("deletechef", name="erhan"),
        follow_redirects=True
    )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'erhan', response.data)

# Testing the CRUD fucntionality on Pizza Model

class TestCRUDPizza(TestBase):

    def test_read_pizza(self):
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
    
    def test_create_pizza(self):
        response = self.client.post(url_for('createpizza'), data=dict(

    name = "Testpizza",
    
    crust = "Thin",
    
    base =  "Tomato",
    
    topping1 = "Chicken",
    
    topping2 = "Pepper hot",
    
    topping3 = "Olives",
    
    topping4 = "Sweetcorn",
    
    topping5 = "Garlic",
    
    chef_id = 1

        ), follow_redirects=True)
        print(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testpizza',response.data)

    
    def test_delete_pizza(self):
        response = self.client.post(url_for('deletepizza', name="pizza"), follow_redirects=True)
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
