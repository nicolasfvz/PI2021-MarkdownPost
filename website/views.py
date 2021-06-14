from flask import Blueprint, render_template, request, flash, jsonify
from flask.globals import request
from flask.helpers import flash, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from werkzeug.utils import redirect
from . import db
import json
from .models import User

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('ademir', methods=['GET', 'POST'])
@login_required
def admin():
    if current_user.id != 1:
        return redirect(url_for('views.home'))

    todos_usuarios = User.query.filter_by().all()
    print(todos_usuarios)
    return render_template('admin.html', user=current_user, usuarios=todos_usuarios)

@views.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html', user=current_user)