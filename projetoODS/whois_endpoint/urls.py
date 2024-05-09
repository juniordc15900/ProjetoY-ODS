from django.urls import path
from . import views

path('check_domains/', views.check_domains, name="check_domains")