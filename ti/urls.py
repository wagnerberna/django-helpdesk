from django import views
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

from ti.views.home import ChangePassword, access_denied, home, logout_user
from ti.views.reports import reports

# Importar views do Django de autenticação
# criar Urls de login e logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("changepassword/", ChangePassword, name="changepassword"),
    path("access_denied/", access_denied, name="access_denied"),
    path("", home, name="home"),
    # path("about/", about),
    path("helpdesk/", include("helpdesk.router.urls_user")),
    path("helpdesk/", include("helpdesk.router.urls_support")),
    path("kanban/", include("kanban.urls")),
    # path("kanban/api/", include("kanban.api.urls")),
    # path("helpdesk/api/", include("helpdesk.api.urls")),
    path("reports/", reports, name="reports"),
]
