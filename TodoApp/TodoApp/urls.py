from django.contrib import admin
from django.urls import path
from todo import views as todo
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todo.get_homepage),
]
