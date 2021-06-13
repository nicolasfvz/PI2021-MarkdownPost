from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/teste', methods=['GET', 'POST'])
def teste():
    logout_user()
    return render_template("test.html", user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", user=current_user)

@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template("cadastro.html", user=current_user)
