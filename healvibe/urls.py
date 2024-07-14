from django.contrib import admin
from django.urls import path, include
from manager import urls

urlpatterns = [
    path("", include("manager.urls")),
    path("admin/", admin.site.urls),
]
