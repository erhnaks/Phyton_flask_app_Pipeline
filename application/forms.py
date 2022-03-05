from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import Chef, Pizza

class Createform(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        name = Chef.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError ('Ooopps, This fantasy chef does exist, Please choose another fancy Chef name')

class Updateform(FlaskForm):
    name = StringField('Chef Name:', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Save')

    def validate_name(self, name):
        name_update_chef = Chef.query.filter_by(name=name.data).first()
        if name_update_chef:
            raise ValidationError ('Ooopps, This fantasy Chef name does exist, Please choose another fancy Chef name')

class Pizzaform(FlaskForm):
    
    name = StringField('Name your custom pizza:', validators=[DataRequired(), Length(min=2, max=30)])
    
    crust = SelectField('Please select crust:', 
    choices=[('Thin', 'Thin'), ('Deep', 'Deep'), ('Stuffed', 'Stuffed')])
    
    base = SelectField('Pizza base:', 
    choices=[('Tomato', 'Tomato'), ('Garlic', 'Garlic'), ('Tomato&Garlic', 'Tomato&Garlic')])
    
    topping1 = SelectField('Meat type:', 
    choices=[('Chicken', 'Chicken'), ('Beef', 'Beef'), ('Tuna', 'Tuna'), ('Vegetarian', 'Vegetarian')])
    
    topping2 = SelectField('Choose a toping:', 
    choices=[('Pepper hot', 'Pepper hot'), ('Pepper mild', 'Pepper mild'), ('Jalapeno', 'Jalapeno')])
    
    topping3 = SelectField('Choose a toping:', 
    choices=[('Olives', 'Olives'), ('Onion', 'Onion'), ('Muhsroom', 'Muhsroom')])
    
    topping4 = SelectField('Choose a toping:', 
    choices=[('Sweetcorn', 'Sweetcorn'), ('Pineapple', 'Pineapple'), ('Sundried Tomato', 'Sundried Tomato')])
    
    topping5 = SelectField('Choose a toping:', 
    choices=[('Garlic', 'Garlic'), ('Capsicum', 'Capsicum'), ('Eggplant', 'Eggplant')])
    
    chef_id = SelectField('Pick your name', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')
    def validate_name(self, name):
        name_pizza = Pizza.query.filter_by(name=name.data).first()
        if name_pizza:
            raise ValidationError ('Ooopps, This fantasy Chef name does exist, Please choose another fancy Chef name')