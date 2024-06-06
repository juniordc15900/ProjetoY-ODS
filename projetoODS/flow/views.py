import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import re
from gemini.models import GeminiAssistant
from godaddy.views import verificar_dominios
from gemini.views import iniciar_chat

def main_flow(request):
    assistant = GeminiAssistant()
    palavras_principais = request.GET['palavras']
    # palavras_principais = ["Floricultura", "Lótus", "Rosas"]
    response = iniciar_chat(palavras_principais,assistant)
    response_data = {'dominios': response}
    print(response_data)
    response = verificar_dominios(response_data)
    return HttpResponse(response)

