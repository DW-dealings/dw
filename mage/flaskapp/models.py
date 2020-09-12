from flask_login import UserMixin
from flaskapp import db, login_manager


user_role = db.Table('user_role',
                     db.Column('emp_id', db.Integer, db.ForeignKey('employees.emp_id'), primary_key=True),
                     db.Column('role_id', db.Integer, db.ForeignKey('roles.role_id'), primary_key=True))


class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    emp_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.dept_id'))
    is_leader = db.Column(db.Boolean, default=False)
    rel_roles = db.relationship('Role', secondary=user_role,
                                backref=db.backref('employee', lazy='dynamic'))

    def get_id(self):
        return self.emp_id

    def __repr__(self):
        return self.username

@login_manager.user_loader
def load_user(emp_id):
    return Employee.query.get(int(emp_id))


class Department(db.Model):
    __tablename__ = 'departments'

    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(222))
    employees = db.relationship('Employee', backref='department', lazy=True)

    def __repr__(self):
        return self.dept_name


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64),unique=True, nullable=False)
    description = db.Column(db.String(222))
    rel_emp = db.relationship('Employee', secondary=user_role,
                              backref=db.backref('role', lazy='dynamic'))

    def __repr__(self):
        return self.role_name


