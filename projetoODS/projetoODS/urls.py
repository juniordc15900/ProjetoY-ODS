from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('adicionar_dominio/', views.adicionar_dominio, name='adicionar_dominio'),
    path('iniciar_sessao/', views.iniciar_sessao, name='iniciar_sessao'),
    path('registrar_clique/', views.registrar_clique, name='registrar_clique'),
    path('listar_dominios/', views.listar_dominios, name='listar_dominios'),
    path('login/', views.login, name='login'),
    path('postsignIn/', views.postsignIn, name='postsignIn'),
    path('logout/', views.logout, name='logout'),
    path('google_login/', views.google_login, name='google_login'),
]