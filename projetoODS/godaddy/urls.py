from django.urls import path
from . import views

urlpatterns = [
    path('verificar', views.verificar_dominios, name="verificar_dominios")

]