from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
auth = Blueprint('auth', __name__)
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Invalid username or password!', category='error')
        else:
            flash('User does\'t exist!', category='error')
    # Pass value to tamplate text='Test'.
    # return render_template('login.html', text="Testing")
    return render_template('login.html', user=current_user)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName= request.form.get('firstName')
        password = request.form.get('password')
        confirmPassword = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')
        elif len(email) < 4 :
            flash('Email require', category='error')
        elif len(firstName) < 2:
           flash('Name require', category='error')
        elif password != confirmPassword:
            flash('Password don\'t match', category='error')
        elif len(password) < 7:
            flash('Password atleast 6 character', category='error')
        else:
            #create new account.
            new_user = User(email=email, firstName=firstName, password= generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)

            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    # Get data from request.
    # data = request.form
    # print(data)
    return render_template('register.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
