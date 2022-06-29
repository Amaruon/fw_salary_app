from flask import Blueprint, request, flash, render_template, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        acronym = request.form.get('acronym')
        password = request.form.get('password')

        user = User.query.filter_by(acronym=acronym).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Acronym does not exist.', category='error')

    return render_template("login.html", user=current_user)
