from application import db
from application.models import Chef, Pizza

db.drop_all()
db.create_all()