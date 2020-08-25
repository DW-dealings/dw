from flask import render_template, flash, g, redirect, url_for, request
from . import appbuilder, db
from flask_appbuilder import expose, has_access, action
from flask_appbuilder.security.views import ResetMyPasswordView, UserInfoEditView
from flask_babel import lazy_gettext
from .forms import ResetPassForm, UpdateUserForm
from flask_appbuilder.security.views import UserDBModelView


class UpdateUsrView(UserInfoEditView):
    form = UpdateUserForm
    form_title = lazy_gettext('Form update')
    form_template = 'update.html'

    def form_get(self, form):
        item = self.appbuilder.sm.get_user_by_id(g.user.id)
        # fills the form generic solution
        for key, value in form.data.items():
            if key == "csrf_token":
                continue
            form_field = getattr(form, key)
            form_field.data = getattr(item, key)

    def form_post(self, form):
        form = self.form.refresh(request.form)
        item = self.appbuilder.sm.get_user_by_id(g.user.id)
        form.populate_obj(item)
        self.appbuilder.sm.update_user(item)
        flash((self.message), "info")


class ResetUsrPassView(ResetMyPasswordView):
    route_base = '/resetusrpass'
    form = ResetPassForm
    form_template = 'reset_password.html'
    form_title = lazy_gettext('Form reset')

    def form_post(self, form):
        self.appbuilder.sm.reset_password(g.user.id, form.password.data)
        flash((self.message), "info")


class MyUserView(UserDBModelView):
    route_base = '/users'

    @expose('/profile')
    @has_access
    def profile(self):
        actions = dict()
        actions['resetusrpass'] = self.actions.get('resetusrpass')
        actions['updateusr'] = self.actions.get('updateusr')
        self.update_redirect()
        return self.render_template('index3.html')

    @action('updateusr', lazy_gettext('Update Account'))
    def updateusr(self):
        return redirect(
            url_for(self.appbuilder.sm.userinfoeditview.__name__ + ".this_form_get")
        )

    @action('resetusrpass', lazy_gettext('Reset Password'))
    def resetusrpass(self):
        return redirect(
            url_for(self.appbuilder.sm.resetmypasswordview.__name__ + ".this_form_get")
        )






"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
appbuilder.add_view(MyUserView, "User", icon='fa-envelope')
appbuilder.add_link("Profile", href='/users/profile', category="User")
