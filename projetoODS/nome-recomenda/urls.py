from django.urls import path

from . import views

urlpatterns = [
    path("nome-recomenda", views.gerarNomes, name="nome-recomenda"),
]