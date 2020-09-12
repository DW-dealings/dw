from flask import render_template, abort
from flask_login import login_required, current_user
from . import home


@home.route('/')
def homepage():
    return render_template('home/index.html', title='Welcome')


@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', title='Dashboard')


@home.route('/leader/dashboard')
@login_required
def leader_dashboard():
    if not current_user.is_leader:
        abort(403)
    return render_template('home/leader_dashboard.html', title='Leader Dashboard')