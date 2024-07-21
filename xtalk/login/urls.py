from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path("", views.login_form, name="form"),
    path("token/<str:token>/", views.check_token, name="check"),
    path("logout/", views.logout_user, name="logout"),
]
