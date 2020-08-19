from flask import Flask
from .forms import RegistrationForm, LoginForm
import os
from .db import db
from .login import login_manager
from .mail import mail

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.urandom(32)
app.config.from_object('config.Config')
db.init_app(app)
mail.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
    db.create_all()

from .models import User
from . import routes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])







