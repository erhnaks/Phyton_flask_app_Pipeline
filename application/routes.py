from application import app, db
from application.models import Pizza, Chef
from application.forms import Createform, Pizzaform, Updateform
from flask import render_template, redirect, url_for, request

@app.route('/createchef', methods = ['POST','GET'])
def createchef():
    createform = Createform()

    if createform.validate_on_submit():
        chef = Chef(name=createform.name.data)
        db.session.add(chef)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('createchef.html', form=createform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
   chef = Chef.query.all()
   return render_template('read.html', chef=chef)

@app.route('/update/<name>', methods=['POST', 'GET'])
def update(name):
    updateform = Updateform()
    chef = Chef.query.filter_by(name=name).first()
    
    if request.method == 'GET':
        updateform.name.data = chef.name
        return render_template('update.html', form=updateform)
    else:
        if updateform.validate_on_submit():
            chef.name = updateform.name.data
            db.session.commit()
            return redirect(url_for('read'))

@app.route('/delete/<name>', methods=['POST', 'GET'])
def delete(name):
        chef = Chef.query.filter_by(name=name).first()
        db.session.delete(chef)
        db.session.commit()
        return redirect(url_for('read'))


@app.route('/create', methods = ['POST','GET'])
def createpizza():
    pizzaform = Pizzaform()
    chef = Chef.query.all()
    for chef in chef:
        pizzaform.chef.choices.append((chef.id, chef.name))

    if pizzaform.validate_on_submit():
        pizza = Pizza(
        name=pizzaform.name.data,
        crust=pizzaform.crust.data,
        base=pizzaform.base.data,
        topping1=pizzaform.topping1.data,
        topping2=pizzaform.topping2.data,
        topping3=pizzaform.topping3.data,
        topping4=pizzaform.topping4.data,
        topping5=pizzaform.topping5.data
        )
        db.session.add(pizza)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create.html', form=pizzaform)
