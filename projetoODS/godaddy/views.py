from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import subprocess
import json

def verificar_disponibilidade(dominios, api_key, api_secret):
    resultados = {}

    for dominio in dominios:
        curl_command = f'curl -X GET -H "Authorization: sso-key {api_key}:{api_secret}" "https://api.ote-godaddy.com/v1/domains/available?domain={dominio}&checkType=FAST&forTransfer=false"'

        try:
            resultado = subprocess.run(curl_command, capture_output=True, text=True, shell=True)
            resposta_json = json.loads(resultado.stdout)
            if resultado.returncode == 0:
                disponivel = resposta_json.get('available', False)
                resultados[dominio] = disponivel
            else:
                resultados[dominio] = False
        except Exception as e:
            resultados[dominio] = False

    return resultados

def verificar_dominios(request):
    api_key = '3mM44UdBmPLDAc_DNoMUWyojvJB8U4XsgyKgv'
    api_secret = 'RuxjJSCVp2BnptYT11AF5X'
    dominios = ['testandositesaquiemcasa.com', 'facebook.com', 'godaddy.com', 'projeto.world', 'projeto2.com', 'gmail.com']
    resultados = verificar_disponibilidade(dominios, api_key, api_secret)

    # Preparar a resposta como um JSON
    response_data = {'resultados': resultados}
    return JsonResponse(response_data)
