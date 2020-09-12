from flask import Blueprint

leader = Blueprint('leader', __name__, url_prefix='/leader')

from . import views