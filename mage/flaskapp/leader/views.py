from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required
from . import leader
from .forms import DepartmentForm, RoleForm, EmployeeAssignForm
from ..models import Department, Role, Employee
from .. import db


def check_leader():
    if not current_user.is_leader:
        abort(403)


@leader.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    check_leader()
    departments = Department.query.all()
    return render_template('leader/departments/departments.html', departments=departments, title='Departments')


@leader.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    check_leader()
    add_department = True
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(dept_name=form.dept_name.data, description=form.description.data)
        if department:
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department')
        return redirect(url_for('leader.list_departments'))
    return render_template('leader/departments/department.html', action='Add',
                           add_department=add_department, form=form, title='Add Department')


@leader.route('/departments/edit/<int:dept_id>', methods=['GET', 'POST'])
@login_required
def edit_department(dept_id):
    check_leader()
    add_department = False
    department = Department.query.get_or_404(dept_id)
    form = DepartmentForm()
    if form.validate_on_submit():
        department.dept_name = form.dept_name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully changed a department')
        return redirect(url_for('leader.list_departments'))
    elif request.method == 'GET':
        form.dept_name.data = department.dept_name
        form.description.data = department.description
    else:
        flash('Cannot change departments')
    return render_template('leader/departments/department.html', action='Edit',
                           add_department=add_department, form=form, department=department,
                           title='Edit Department')


@leader.route('/departments/delete/<int:dept_id>', methods=['GET', 'POST'])
@login_required
def delete_department(dept_id):
    check_leader()
    department = Department.query.get_or_404(dept_id)
    if department:
        db.session.delete(department)
        db.session.commit()
        flash('You have successfully deleted a department')
        return redirect(url_for('leader.list_departments'))
    return render_template(title='Delete Department')


@leader.route('/roles')
@login_required
def list_roles():
    check_leader()
    roles = Role.query.all()
    return render_template('leader/roles/roles.html', roles=roles, title='Roles')


@leader.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    check_leader()
    add_role = True
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(role_name=form.role_name.data, description=form.description.data)
        if role:
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role')
        return redirect(url_for('leader.list_roles'))
    return render_template('leader/roles/role.html', action='Add',
                           add_role=add_role, form=form, title='Add Role')


@leader.route('/roles/edit/<int:role_id>', methods=['GET', 'POST'])
@login_required
def edit_role(role_id):
    check_leader()
    add_role = False
    role = Role.query.get_or_404(role_id)
    form = RoleForm()
    if form.validate_on_submit():
        role.role_name = form.role_name.data
        role.description = form.description.data
        db.session.commit()
        flash('You have successfully changed a role')
        return redirect(url_for('leader.list_roles'))
    elif request.method == 'GET':
        form.role_name.data = role.role_name
        form.description.data = role.description
    else:
        flash('Cannot change roles')
    return render_template('leader/roles/role.html', action='Edit',
                           add_role=add_role, form=form, role=role,
                           title='Edit Role')


@leader.route('/roles/delete/<int:role_id>', methods=['GET', 'POST'])
@login_required
def delete_role(role_id):
    check_leader()
    role = Role.query.get_or_404(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        flash('You have successfully deleted a role')
        return redirect(url_for('leader.list_roles'))
    return render_template(title='Delete Role')


@leader.route('/employees')
@login_required
def list_employees():
    check_leader()
    employees = Employee.query.all()
    return render_template('leader/employees/employees.html', title='List Employee', employees=employees)


@leader.route('/employees/delete/<int:emp_id>', methods=['GET', 'POST'])
@login_required
def delete_employee(emp_id):
    check_leader()
    employee = Employee.query.get_or_404(emp_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        flash('You have successfully deleted a employee')
        return redirect(url_for('leader.list_employees'))
    return render_template(title='Delete Employee')


@leader.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    check_leader()
    employee = Employee.query.get_or_404(id)
    form = EmployeeAssignForm()
    if form.validate_on_submit():
        role = Role(role_id=form.data.get('role').role_id)
        employee.role.append(role)
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned role to employee')
        return redirect(url_for('leader.list_employees'))
    else:
        flash('No hope')
    return render_template('leader/employees/employee.html', form=form,
                           title='Assign Employee')





