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


class EmployeeAssignForm(FlaskForm):
    role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label='role_name')
    user = QuerySelectField(query_factory=lambda: Employee.query.all(), get_label='emp_id')
    submit = SubmitField('Submit')
