from django.urls import path

from . import views

app_name = "merch"

urlpatterns = [
    path("", views.merch, name="merch"),
    path("quiz/", views.quiz, name="quiz"),
]
