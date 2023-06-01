from website import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150))
    name = db.Column(db.String(150))
    type = db.Column(db.String(150))
    size = db.Column(db.Float)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    description = db.Column(db.String(1000)) 
    rating = db.Column(db.Float)
    rating_count = db.Column(db.Integer)

class Notes(db.Model):
    note_id = db.Column(db.Integer,primary_key=True)
    note_name = db.Column(db.String(150))
    description = db.Column(db.String(1000))



class ProductNotes(db.Model):
    __tablename__ = 'product_notes'
    
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('notes.note_id'), primary_key=True)
    
    product = db.relationship('Product', backref=db.backref('product_notes', cascade='all, delete-orphan'))
    note = db.relationship('Notes', backref=db.backref('product_notes', cascade='all, delete-orphan'))



class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Float)
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.Column(db.Text)

    user = db.relationship('User', backref='comments')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.Text)
    rating = db.Column(db.Integer)
    date = db.Column(db.Date)


    product = db.relationship('Product', backref=db.backref('reviews', lazy=True))
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
