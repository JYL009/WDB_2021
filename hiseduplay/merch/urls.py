from django.urls import path
from . import views

urlpatterns = [
    path('', views.merch),
    path('quiz/', views.quiz)
]