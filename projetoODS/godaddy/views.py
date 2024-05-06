from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import subprocess
import json
import time
from concurrent.futures import ThreadPoolExecutor

def verificar_disponibilidade_threads(dominio, api_key, api_secret):
    curl_command = f'curl -X GET -H "Authorization: sso-key {api_key}:{api_secret}" "https://api.ote-godaddy.com/v1/domains/available?domain={dominio}&checkType=FAST&forTransfer=false"'
    try:
        inicio = time.time()
        resultado = subprocess.run(curl_command, capture_output=True, text=True, shell=True)
        fim = time.time()
        duracao = fim - inicio
        resposta_json = json.loads(resultado.stdout)
        if resultado.returncode == 0:
            disponivel = resposta_json.get('available', False)
            return {'disponivel': disponivel, 'duracao': duracao}
        else:
            return f"Erro ao verificar: {resposta_json.get('message', 'Erro desconhecido')}"
    except Exception as e:
        return f"Erro ao verificar: {e}"

def verificar_dominios_threads(request):
    api_key = '3mM44UdBmPLDAc_DNoMUWyojvJB8U4XsgyKgv'
    api_secret = 'RuxjJSCVp2BnptYT11AF5X'
    dominios = ['testandositesaquiemcasa.com', 'facebook.com', 'godaddy.com', 'projeto.world', 'projeto2.com','gmail.com','drive.google.com','web.whatsapp.com','developer.godaddy.com','twitter.com',
                'testy.com.br','testy.com','testy.co','testy.org','testy.net','testy.inc','testy.es','testy.web','testy.uk','testy.io',
                'testy2.com.br','testy2.com','testy2.co','testy2.org','testy2.net','testy2.inc','testy2.es','testy2.web','testy2.uk','testy2.io',
                'testy3.com.br','testy3.com','testy3.co','testy3.org','testy3.net','testy3.inc','testy3.es','testy3.web','testy3.uk','testy3.io',
                'testy4.com.br','testy4.com','testy4.co','testy4.org','testy4.net','testy4.inc','testy4.es','testy4.web','testy4.uk','testy4.io',
                'testy5.com.br','testy5.com','testy5.co','testy5.org','testy5.net','testy5.inc','testy5.es','testy5.web','testy5.uk','testy5.io',
                'testy6.com.br','testy6.com','testy6.co','testy6.org','testy6.net','testy6.inc','testy6.es','testy6.web','testy6.uk','testy6.io',
                'testy7.com.br','testy7.com','testy7.co','testy7.org','testy7.net','testy7.inc','testy7.es','testy7.web','testy7.uk','testy7.io',
                'testy8.com.br','testy8.com','testy8.co','testy8.org','testy8.net','testy8.inc','testy8.es','testy8.web','testy8.uk','testy8.io',
                'testy9.com.br','testy9.com','testy9.co','testy9.org','testy9.net','testy9.inc','testy9.es','testy9.web','testy9.uk','testy9.io',
                'floresazuis.com.br']
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Executar a função verificar_disponibilidade() em paralelo para cada domínio
        resultados = {dominio: executor.submit(verificar_disponibilidade_threads, dominio, api_key, api_secret) for dominio in dominios}

        # Aguardar que todas as threads sejam concluídas e obter os resultados
        for dominio, resultado in resultados.items():
            resultados[dominio] = resultado.result()

    response_data = {'resultados': resultados}
    return JsonResponse(response_data)

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
