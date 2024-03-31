from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship 


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///khushi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mname = db.Column(db.String(50))
    subscription = db.Column(db.Boolean)


class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    total = db.Column(db.Integer)
    ord_name = db.Column(db.String(70))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.bid'))
    blog = db.relationship("Blog", back_populates="orders")
    

class Blog(db.Model):
    bid = db.Column(db.Integer,primary_key=True)
    bname=db.Column(db.String(70))
    content = db.Column(db.String(100))

if __name__ == '__main__':
    app.run(debug=True)


