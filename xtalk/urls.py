from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", include("xtalk.login.urls")),
    path("", views.home, name="home"),
    path("room/<uuid:room>/", views.room, name="room"),
]

if settings.BROWSER_RELOAD:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
