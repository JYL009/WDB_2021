from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.question_list),
    path('write/', views.question_write),
    path('detail/<str:question_id>', views.question_detail),
    path('answer_write/<str:question_id>', views.answer_write),
]