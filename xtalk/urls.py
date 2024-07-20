from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.BROWSER_RELOAD:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
