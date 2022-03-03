from application import db

class Chef(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    chef_pizza = db.relationship('Pizza', backref='chef')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    crust = db.Column(db.String(100), nullable=False)
    base = db.Column(db.String(100), nullable=False)
    topping1 = db.Column(db.String(100), nullable=False)
    topping2 = db.Column(db.String(100), nullable=False)
    topping3 = db.Column(db.String(100), nullable=False)
    topping4 = db.Column(db.String(100), nullable=False)
    topping5 = db.Column(db.String(100), nullable=False)
    chef_id = db.Column(db.Integer, db.ForeignKey('chef.id'))
    


