from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import StringField, PasswordField, ValidationError, SubmitField
from .models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username Required')])
    email = StringField('Email', validators=[DataRequired(message='Email Required'), Email()])
    firstname = StringField('Firstname', validators=[DataRequired(message='First name Required')])
    lastname = StringField('Lastname', validators=[DataRequired(message='Last name Required')])
    password = PasswordField('Password', validators=[DataRequired(message='Password Required')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message='Re-enter password'),
                                                                     EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken , please choose another')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken , please choose another')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username Required')])
    password = PasswordField('Password', validators=[DataRequired(message='Password Required')])
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username Required')])
    email = StringField('Email', validators=[DataRequired(message='Email Required'), Email()])
    firstname = StringField('Firstname', validators=[DataRequired(message='First name Required')])
    lastname = StringField('Lastname', validators=[DataRequired(message='Last name Required')])
    submit = SubmitField('Change')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken , please choose another')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken , please choose another')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(message='Password Required')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message='Re-enter password'),
                                                                     EqualTo('password')])
    submit = SubmitField('Reset Password')

