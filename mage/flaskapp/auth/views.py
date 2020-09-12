from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, current_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(username=form.username.data,
                            email=form.email.data,
                            firstname=form.firstname.data,
                            lastname=form.lastname.data,
                            password=form.password.data)

        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered, you can now able to login')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(username=form.username.data, password=form.password.data).first()
        if employee:
            login_user(employee, remember=False)
            if employee.is_leader:
                return redirect(url_for('home.leader_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:
            flash('Incorrect log in')
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out')
    return redirect(url_for('auth.login'))