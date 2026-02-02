
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.quiz_list,name="quiz_list"),
    path("quiz_detail/<int:id>",views.quiz_detail,name="quiz_detail"),
    path("quiz/<int:id>",views.start_quiz,name="start_quiz"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
