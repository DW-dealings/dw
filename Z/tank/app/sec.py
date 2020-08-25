from flask_appbuilder.security.sqla.manager import SecurityManager
from .views import ResetUsrPassView, UpdateUsrView, MyUserView


class MySec(SecurityManager):
    resetmypasswordview = ResetUsrPassView
    userinfoeditview = UpdateUsrView
    userdbmodelview = MyUserView