from flask_appbuilder.forms import DynamicForm
from wtforms import StringField, PasswordField, ValidationError, SubmitField
from wtforms.validators import DataRequired, EqualTo


class UpdateUserForm(DynamicForm):
    usrname = StringField('Username', validators=[DataRequired(message='Nhap username')])
    firstname = StringField('Firstname', validators=[DataRequired(message='nhap ten dau')])
    lastname = StringField('Lastname', validators=[DataRequired(message='nhap ten sau')])
    submit = SubmitField('Change')


class ResetPassForm(DynamicForm):
    usrpass = PasswordField('Password', validators=[DataRequired(message='nhap pass')])
    confirm_pass = StringField('Confirm password', validators=[DataRequired(message='nhap lai pass'),
                                                               EqualTo('usrpass')])

    submit = SubmitField('Change')



