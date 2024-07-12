from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("list-users/", views.list_users, name="list_users"),
    path("add-user/", views.add_user, name="add_user"),
]
