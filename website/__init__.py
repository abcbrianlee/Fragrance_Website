from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefg'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + DB_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/abcbrianlee/CS Folder/ECommerce_Site/database.db'
    db.init_app(app)



    from .views import views
    from .auth import auth
    from .product import product_bp, Product

    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')


    from .models import User, Note, Product

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))    



    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')