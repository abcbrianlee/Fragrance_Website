from flask import Blueprint, render_template
from flask_login import current_user
from .models import Product
from . import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/cologne')
def cologne_page():
    products = Product.query.filter_by(type='cologne').all()
    
    return render_template("cologne.html", user=current_user, products=products)

@product_bp.route('/perfume')
def perfume_page():
    products = Product.query.filter_by(type='perfume').all()

    return render_template("perfume.html", user=current_user, products=products)

@product_bp.route('/cologne_detail/<int:product_id>')
def cologne_detail_page(product_id):
    product = Product.query.get_or_404(product_id)

    return render_template("cologne_detail.html", user=current_user, product=product)

@product_bp.route('/cologne_brand/<string:product_brand>')
def cologne_brand_page(product_brand):
    products = Product.query.filter_by(brand=product_brand).all()
  
    
    return render_template("cologne_brand.html", user=current_user, products=products, brand=product_brand)

@product_bp.route('/perfume_detail/<int:product_id>')
def perfume_detail_page(product_id):
    product = Product.query.get_or_404(product_id)

    return render_template("perfume_detail.html", user=current_user, product=product)

@product_bp.route('/perfume_brand/<string:product_brand>')
def perfume_brand_page(product_brand):
    products = Product.query.filter_by(brand=product_brand).all()
  
    
    return render_template("perfume_brand.html", user=current_user, products=products, brand=product_brand)