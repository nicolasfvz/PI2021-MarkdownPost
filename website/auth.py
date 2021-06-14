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
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')
        check = request.form.get('check')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, senha):
                flash('Você se logou!', category='success')
                if check != None:
                    login_user(user, remember=True)
                else:
                    login_user(user, remember=False)
                
                return redirect(url_for('views.home'))
            else:
                flash('Senha errada!', category='error')
        else:
            flash('Usuario não encontrado!', category='error')

        print(email)
        print(senha)
        print(check)
        return render_template("teste.html", user=current_user)
    return render_template("teste.html", user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')
        check = request.form.get('check')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, senha):
                flash('Você se logou!', category='success')
                if check != None:
                    login_user(user, remember=True)
                else:
                    login_user(user, remember=False)
                if user.id == 1:
                    login_user(user, remember=False)
                    return redirect(url_for('views.admin'))
                return redirect(url_for('views.user'))
            else:
                flash('Senha errada!', category='error')
        else:
            flash('Usuario não encontrado!', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('name')
        senha1 = request.form.get('password1')
        senha2 = request.form.get('password2')
        check = request.form.get('check')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email já esta cadastrado!', category='error')
        elif len(email) < 4:
            flash('Email muito pequeno! (Deve ser maior que 4 caracteres)', category='error')
        elif len(nome) < 2:
            flash('Nome muito pequeno! (Deve ser maior que 2 caracteres)', category='error')
        elif senha1 != senha2:
            flash('Verifique se as senhas são as mesmas!', category='error')
        elif len(senha1) < 7:
            flash('Sua senha é muito pequena! (Deve ser maior que 7 caracteres)', category='error')
        else:
            #Adicionar data base

            new_user = User(email=email, name=nome, password=generate_password_hash(senha1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            if check != None:
                login_user(new_user, remember=True)
            else:
                login_user(new_user, remember=False)

            flash('Sua conta foi criada!', category='success')

            return redirect(url_for('views.user'))
    return render_template("cadastro.html", user=current_user)
