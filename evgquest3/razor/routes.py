from flaskr import app
from flask import render_template, redirect, url_for, flash, request
from .models import User
from .forms import RegistrationForm, LoginForm, UpdateAccountForm, ResetPasswordForm
from flask_login import current_user
from .db import db
from .mail import mail
from flask_login import login_user, logout_user, login_required
from flask_mail import Message


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Docker Python', name='Lamp Light')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been registered , you are now able to log in')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            login_user(user, remember=False)
            return redirect(url_for('profile'))
        else:
            flash('Login failed')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        db.session.commit()
        flash('Your account has been updated')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
    return render_template('account.html', title='Profile', form=form)


@app.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        current_user.password = form.password.data
        db.session.commit()
        flash('Your password has been changed')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.password.data = current_user.password
    return render_template('reset_password.html', title='Reset Password', form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('index3.html')


@app.route('/send_mail', methods=['GET', 'POST'])
@login_required
def send_mail():
    msg = Message('Verification email', recipients=['ainzquang@gmail.com'])
    mail.send(msg)
    return 'Message Sent!'