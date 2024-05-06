from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('verificar/', views.verificar_dominios, name="verificar_dominios"),
    path('verificar_threads/', views.verificar_dominios_threads, name="verificar_dominios_threads")
=======
    path('verificar', views.verificar_dominios, name="verificar_dominios")
>>>>>>> c86ae04258a0153cb23122bda5648e4eb017a5ef

]