from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def print_teste(request):
    return HttpResponse("Teste de Endpoint")