from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#help sqlalchamy to connect with database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sample.sqlite3"
db = SQLAlchemy(app)
app.app_context().push()

class Brand(db.Model):
    b_id = db.Column(db.Integer, primary_key = True)
    b_name = db.Column(db.String(30),nullable = False)
    cars = db.relationship("Car",backref="company")

class Car(db.Model):
    c_id = db.Column(db.Integer, primary_key = True)
    c_name = db.Column(db.String(30),nullable = False)
    maker = db.Column(db.Integer, db.ForeignKey("brand.b_id"))


#CRUD
# b1 = Brand(b_name = "TESLA" )#create
# c1 = Car(c_name = "model S")
# db.session.add_all([b1,c1])
# db.session.commit()
# mycar = Car.query.all()#read
# second = mycar[0]
# second.c_name = "model z" #update
# db.session.commit()
# to_delete = Car.query.filter_by(c_name = "model z").first()
# db.session.delete(to_delete)#delete
# db.session.commit()