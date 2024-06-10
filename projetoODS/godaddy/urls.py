from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_dominios, name="verificar_dominios"),
    path('verificar_threads/', views.verificar_dominios_threads, name="verificar_dominios_threads"),
    path('compra_dominio/', views.compra_dominio, name="compra_dominio")

]