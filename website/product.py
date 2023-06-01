from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from .models import Product, Notes, ProductNotes, Comment, Rating, User, Review
from . import db
from sqlalchemy import text, func
from datetime import datetime
from datetime import date

product_bp = Blueprint('product', __name__)

@product_bp.route('/cologne')
def cologne_page():
    products = Product.query.filter_by(type='cologne').all()
    notes = Notes.query.all()
    productNotes = ProductNotes.query.all()
    reviews = Review.query.all()


    
    return render_template("cologne.html", user=current_user, products=products, notes=notes,productNotes=productNotes, reviews=reviews)

@product_bp.route('/perfume')
def perfume_page():
    products = Product.query.filter_by(type='perfume').all()
    notes = Notes.query.all()
    productNotes = ProductNotes.query.all()

    return render_template("perfume.html", user=current_user, products=products,notes=notes,productNotes=productNotes)

@product_bp.route('notes')
def notes_library_page():
    notes = Notes.query.all()

    return render_template("notes_library.html", user =current_user, notes=notes)

@product_bp.route('/cologne_detail/<int:product_id>')
def cologne_detail_page(product_id):
    product = Product.query.get_or_404(product_id)
    notes = Notes.query.all()
    productNotes = ProductNotes.query.all()
    users = User.query.all()
    reviews = Review.query.filter_by(product_id=product_id).all()
    

    return render_template("cologne_detail.html", user=current_user, product=product, notes=notes, productNotes=productNotes,users=users, reviews=reviews)

@product_bp.route('/cologne_brand/<string:product_brand>')
def cologne_brand_page(product_brand):
    products = Product.query.filter_by(brand=product_brand).all()
    notes = Notes.query.all()
    productNotes = ProductNotes.query.all()
  
    
    return render_template("cologne_brand.html", user=current_user, products=products, brand=product_brand,notes=notes,productNotes=productNotes)

@product_bp.route('/perfume_detail/<int:product_id>')
def perfume_detail_page(product_id):
    product = Product.query.get_or_404(product_id)
    notes= Notes.query.all()
    productNotes=ProductNotes.query.all()
    users = User.query.all()
    reviews = Review.query.filter_by(product_id=product_id).all()

    return render_template("perfume_detail.html", user=current_user, product=product, notes=notes,productNotes=productNotes, users=users, reviews=reviews)

@product_bp.route('/perfume_brand/<string:product_brand>')
def perfume_brand_page(product_brand):
    products = Product.query.filter_by(brand=product_brand).all()
    notes = Notes.query.all()
    productNotes=ProductNotes.query.all()
  
    
    return render_template("perfume_brand.html", user=current_user, products=products, brand=product_brand,notes=notes,productNotes=productNotes)

@product_bp.route('/notes/<note_id>')
def notes_page(note_id):
    notes = Notes.query.filter_by(note_id=note_id).all()
    product_notes=ProductNotes.query.all()
    products=Product.query.all()

    return render_template("notes_detail.html", user=current_user, products=products, product_notes=product_notes, notes=notes, note=note_id)

@product_bp.route('/store-comment', methods=['POST'])
def store_comment():
    comment_text = request.json.get('comment')
    product_id = request.json.get('product_id')
    user_id = request.json.get('user_id')
    rating_value = request.json.get('rating')
    current_date = date.today()
    

    comment = Review(comment=comment_text, product_id=product_id, user_id=user_id,rating=rating_value, date=current_date)
    db.session.add(comment)
    db.session.commit()

    product = Product.query.get_or_404(product_id)
    product.rating_count += 1

    rating_count = product.rating_count

    total_rating = db.session.query(func.sum(Review.rating)).filter_by(product_id=product_id).scalar()
    new_rating = ( total_rating) / (rating_count )

    product.rating = new_rating

    db.session.commit()


    
    return jsonify({'message': 'Comment stored successfully'})

