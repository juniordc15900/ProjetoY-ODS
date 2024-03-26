from django.urls import path

from . import views

urlpatterns = [
    path("teste", views.print_teste, name="print_teste"),
]