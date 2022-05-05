
from django.urls import path
from core import views

urlpatterns = [
    path("", views.index),
    path("disciplinas/<str:disciplina>", views.disciplina),
    path("busca/<int:page>", views.busca),
]
