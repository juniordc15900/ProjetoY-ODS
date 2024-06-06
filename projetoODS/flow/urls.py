from django.urls import path

from . import views

urlpatterns = [
    path("flow", views.main_flow, name="flow"),
]