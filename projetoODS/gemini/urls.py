from django.urls import path

from . import views

urlpatterns = [
    path("gemini-dominios", views.gemini_dominios, name="gemini-dominios"),
    path("teste", views.teste, name="teste"),
]