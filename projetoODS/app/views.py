from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from app.models import ExemploEntidade


def print_teste(request):
    pessoa = ExemploEntidade(nome='alessandro', sobrenome='dangelo')
    return HttpResponse(f'Nome : {pessoa.nome} {pessoa.sobrenome}')