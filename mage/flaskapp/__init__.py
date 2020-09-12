import os
from flask import Flask
from .db import db
from .mail import mail
from .login import login_manager
from .migrate import migrate
from .leader import leader
from .auth import auth
from .home import home
from .bootstrap import bootstrap

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.urandom(32)
app.config.from_object('config.Config')
db.init_app(app)
mail.init_app(app)
migrate.init_app(app, db)
bootstrap.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must be logged in to access this page'

app.register_blueprint(leader)
app.register_blueprint(auth)
app.register_blueprint(home)

with app.app_context():
    db.create_all()

from .models import Employee, Department, Role, user_role

