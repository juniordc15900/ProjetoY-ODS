from django.urls import path

from . import views

urlpatterns = [
    path("gemini-nome-recomenda", views.gerarNomes, name="gemini-nome-recomenda"),
]