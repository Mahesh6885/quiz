
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register/<int:id>",views.start)
]
