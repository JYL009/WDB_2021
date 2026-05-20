from django.urls import path

from . import views

app_name = "qna"

urlpatterns = [
    path("list/", views.question_list, name="list"),
    path("write/", views.question_write, name="write"),
    path("detail/<int:question_id>/", views.question_detail, name="detail"),
    path("answer_write/<int:question_id>/", views.answer_write, name="answer_write"),
]
