from django.urls import path

from . import views

app_name = "member"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
]
