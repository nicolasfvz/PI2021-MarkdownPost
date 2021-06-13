from flask import Blueprint, render_template, request, flash, jsonify
from flask.globals import request
from flask.helpers import flash
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)
