# AJUSTAR AS FUNÇÕES INSERIDAS E REMOVER AS FUNÇÕES ANTIGAS

import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import re
from gemini.models import GeminiAssistant
from godaddy.views import verificar_dominios
import random
from langdetect import detect
from google.api_core.exceptions import ResourceExhausted
import time

def gemini_dominios(request):
    assistant = GeminiAssistant()
    palavras_principais = request.GET['palavras']
    # palavras_principais = ["Floricultura", "Lótus", "Rosas"]
    response = iniciar_chat(palavras_principais,assistant)
    response_data = {'dominios': response}
    print(response_data)
    response = verificar_dominios(response_data)
    return HttpResponse(response)
def teste(request):
    return HttpResponse('testou e deu certo')

def iniciar_chat(palavras_principais, assistant: GeminiAssistant):
    bem_vindo = "##"
    print(len(bem_vindo) * "#")
    print(bem_vindo)

    while True:
        palavras_relacionadas = assistant.gerar_palavras_relacionadas(palavras_principais)
        palavras_relacionadas_lista = palavras_relacionadas.split('\n')
        palavras = [p.lower().replace('-', '') for p in palavras_relacionadas_lista if p.strip()]

        dominios = gerar_dominios(palavras, assistant.extensao_dominio)

        print("Domínios:")
        for dominio in dominios:
            print(dominio)

            # Selecionar um domínio aleatório da lista gerada
        dominio_interesse = random.choice(dominios).split('.')[0]

        adjetivos = gerar_adjetivos_aleatorios(assistant)
        if not adjetivos:
            print("Erro ao gerar adjetivos. Tentando novamente.")
            continue
        print(f"Adjetivos aleatórios selecionados: {', '.join(adjetivos)}")

            # Geração de domínios modificados com base nos adjetivos aleatórios
        dominios_modificados = gerar_dominios_modificados_com_adjetivos(dominio_interesse, "", adjetivos, assistant)

        if not dominios_modificados:
            print("Nenhum domínio modificado foi gerado com os adjetivos/palavras fornecidos.")
        else:
            print("Domínios melhorados:")
            for dominio in dominios_modificados:
                # Remover numeração e asteriscos
                dominio_limpo = re.sub(r'^[0-9]+\.\s*\*\s*', '', dominio).strip()
                print(dominio_limpo)

        break  # Encerrar o loop após uma interação

    print("Encerrando chat!")

def gerar_dominios(palavras, extensoes):
        dominios = []
        for palavra in palavras:
            palavra_sem_acentos = re.sub(r'[áàâãä]', 'a', palavra, flags=re.IGNORECASE)
            palavra_sem_acentos = re.sub(r'[éèêë]', 'e', palavra_sem_acentos, flags=re.IGNORECASE)
            palavra_sem_acentos = re.sub(r'[íìîï]', 'i', palavra_sem_acentos, flags=re.IGNORECASE)
            palavra_sem_acentos = re.sub(r'[óòôõö]', 'o', palavra_sem_acentos, flags=re.IGNORECASE)
            palavra_sem_acentos = re.sub(r'[úùûü]', 'u', palavra_sem_acentos, flags=re.IGNORECASE)
            palavra_sem_acentos = re.sub(r'[ç]', 'c', palavra_sem_acentos, flags=re.IGNORECASE)
            palavra_sem_acentos = re.sub(r'[^a-zA-Z0-9-_]', '', palavra_sem_acentos)  
            palavra_sem_acentos = palavra_sem_acentos.replace(' ', '_').replace('--', '-').strip('-_') 
            for extensao in extensoes:
                if extensao.startswith('.'):
                    extensao = extensao[1:]
                dominios.append(f"{palavra_sem_acentos}.{extensao}")
        return random.sample(dominios, min(20, len(dominios)))

def gerar_dominios_modificados_com_adjetivos(dominio_interesse, explicacao, adjetivos, assistant: GeminiAssistant): # NOVA FUNÇÃO A SER MODIFICADA PARA A BRANCH
    prompt = f"A partir do domínio {dominio_interesse} e da descrição do negócio: {explicacao}, gere uma lista de 10 domínios melhorados incorporando as seguintes palavras/adjetivos: {', '.join(adjetivos)}."

    try:
        resposta = assistant.model.generate_content(prompt)
        time.sleep(2)  # Pausa de 2 segundos entre as requisições

        # Verificação se o campo 'text' está presente na resposta
        if hasattr(resposta, 'text'):
            dominios_modificados = resposta.text.strip().split('\n')
        else:
            print("A resposta não contém o campo 'text'. Verifique as classificações de segurança do candidato.")
            dominios_modificados = []

    except ResourceExhausted as e:
        print(f"Erro: Limite de requisições excedido. {e}")
        dominios_modificados = []

    # Remover caracteres indesejados e adicionar extensões aleatórias
    dominios_limpos = []
    for dominio in dominios_modificados:
        dominio = re.sub(r'^[0-9]+\.\s*', '', dominio).strip()  # Remove numeração
        dominio = re.sub(r'\*\*Domain:\*\*\s*|\*\*$', '', dominio).strip()  # Remove '**Domain:**' e '**'
        dominio = dominio.replace("..", ".")  # Corrige a ocorrência de '..'
        for extensao in random.sample(assistant.extensao_dominio, 5):
            if extensao.startswith('.'):
                extensao = extensao[1:]
            dominios_limpos.append(f"{dominio}.{extensao}")

    return random.sample(dominios_limpos, min(20, len(dominios_limpos)))

def gerar_palavras_relacionadas(palavras_principais, assistant: GeminiAssistant): #AJUSTAR PARA A BRANCH
    palavras_string = ', '.join(palavras_principais)
    lingua_dominante = detect(palavras_string)

    if lingua_dominante == 'pt':
        prompt_palavras_relacionadas = f"A partir da lista {palavras_string}, gere uma nova lista para cada item com 10 sinônimos/palavras relacionadas em português seguindo o seguinte modelo:\n\nPalavra1 (Português)\nSinônimo1 (Português)\nSinônimo2 (Português)\nSinônimo3 (Português)\nSinônimo4 (Português)\n...\nSinônimo10 (Português)"
    else:
        prompt_palavras_relacionadas = f"A partir da lista {palavras_string}, gere uma nova lista para cada item com 10 sinônimos/palavras relacionadas em inglês e português seguindo o seguinte modelo:\n\nPalavra1 (Português)\nSinônimo1 (Português)\nSinônimo2 (Português)\nSinônimo3 (Português)\nSinônimo4 (Português)\n...\nSinônimo10 (Português)\n\nPalavra1 (English)\nSinônimo1 (English)\nSinônimo2 (English)\nSinônimo3 (English)\nSinônimo4 (English)\n...\nSinônimo10 (English)"
        
    try:
        resposta = assistant.model.generate_content(prompt_palavras_relacionadas)
        time.sleep(2)  # Pausa de 2 segundos entre as requisições

        if hasattr(resposta, 'text'):
            palavras_relacionadas = resposta.text.strip()
        else:
            print("A resposta não contém o campo 'text'. Verifique as classificações de segurança do candidato.")
            palavras_relacionadas = ""

    except ResourceExhausted as e:
        print(f"Erro: Limite de requisições excedido. {e}")
        palavras_relacionadas = ""

    return palavras_relacionadas

def gerar_adjetivos_aleatorios(assistant: GeminiAssistant): # AJUSTAR PARA A BRANCH
    prompt = "Gere uma lista de 10 adjetivos em português que podem ser usados para melhorar nomes de domínio."
    try:
        resposta = assistant.model.generate_content(prompt)
        time.sleep(2)  # Pausa de 2 segundos entre as requisições
            
        if hasattr(resposta, 'text'):
            adjetivos_possiveis = resposta.text.strip().split('\n')
            adjetivos_aleatorios = random.sample(adjetivos_possiveis, 3)
        else:
            print("A resposta não contém o campo 'text'. Verifique as classificações de segurança do candidato.")
            adjetivos_aleatorios = []
    except ResourceExhausted as e:
        print(f"Erro: Limite de requisições excedido. {e}")
        adjetivos_aleatorios = []

    return adjetivos_aleatorios