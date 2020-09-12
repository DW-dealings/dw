from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Role, Department, Employee
from ..db import db


class DepartmentForm(FlaskForm):
    dept_name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')


class RoleForm(FlaskForm):
    role_name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')


def possible_role():
    return Role.query.all()


class EmployeeAssignForm(FlaskForm):
    role = QuerySelectField(query_factory=possible_role, get_label='role_id')
    submit = SubmitField('Submit')