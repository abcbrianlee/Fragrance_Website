from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Notes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    notes = Notes.query.all()

    return render_template("home.html", user=current_user, notes=notes)

