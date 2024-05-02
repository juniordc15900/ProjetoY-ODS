import json
from django.http import JsonResponse
from django.shortcuts import render
import re
from gemini.models import GeminiAssistant

def gemini_dominios(request):
    assistant = GeminiAssistant()
    
    body_bytes = request.body
    body_str = body_bytes.decode('utf-8')
    json_data = json.loads(body_str)
    
    palavras_principais = json_data.get('palavras')
    # palavras_principais = ["Floricultura", "Lótus", "Rosas"]
    response = iniciar_chat(palavras_principais,assistant)
    response_data = {'dominios': response}
    return JsonResponse(response_data)
def iniciar_chat(palavras_principais,assistant:GeminiAssistant):
        bem_vindo = "##"
        print(len(bem_vindo) * "#")
        print(bem_vindo)

        palavras_relacionadas = gerar_palavras_relacionadas(palavras_principais,assistant)
        palavras_relacionadas_lista = palavras_relacionadas.split('\n')
        palavras = [p.lower().replace('-', '') for p in palavras_relacionadas_lista if p.strip()]  

        extensoes_br = ["com.br", "net.br", "org.br", "com", "br", "net"]  
        dominios_br = gerar_dominios(palavras, extensoes_br)
        return dominios_br

def translate_to_english(self, word):
    translation = self.translator.translate(word, src='pt', dest='en')
    return translation.text

def translate_to_portuguese(self, words):
    translations = []
    for word in words:
        translation = self.translator.translate(word, src='en', dest='pt')
        translations.append(translation.text)
    return translations

def gerar_dominios(palavras, extensoes):
    dominios = []
    for palavra in palavras:
        palavra_sem_acentos = re.sub(r'[áàâãä]', 'a', palavra, flags=re.IGNORECASE)
        palavra_sem_acentos = re.sub(r'[éèêë]', 'e', palavra_sem_acentos, flags=re.IGNORECASE)
        palavra_sem_acentos = re.sub(r'[íìîï]', 'i', palavra_sem_acentos, flags=re.IGNORECASE)
        palavra_sem_acentos = re.sub(r'[óòôõö]', 'o', palavra_sem_acentos, flags=re.IGNORECASE)
        palavra_sem_acentos = re.sub(r'[úùûü]', 'u', palavra_sem_acentos, flags=re.IGNORECASE)
        palavra_sem_acentos = re.sub(r'[ç]', 'c', palavra_sem_acentos, flags=re.IGNORECASE)
        palavra_sem_acentos = re.sub(r'[^a-zA-Z0-9-]', '', palavra_sem_acentos)  
        palavra_sem_acentos = palavra_sem_acentos.replace(' ', '-')  
        for extensao in extensoes:
            dominios.append(f"{palavra_sem_acentos}.{extensao}")
    return dominios

def gerar_palavras_relacionadas(palavras,assistant: GeminiAssistant):
    palavras_string = ", ".join(palavras)
    prompt_palavras_relacionadas = f"A partir da lista {palavras_string}, gere uma nova lista para cada item com 10 sinônimos/palavras relacionadas seguindo o seguinte modelo:\n\nPalavra1\nSinônimo1\nSinônimo2\nSinônimo3\nSinônimo4\n...\nSinônimo10\n\nPalavra2\nSinônimo1\nSinônimo2\nSinônimo3\nSinônimo4\n...\nSinônimo10\n\nPalavra3\n...\n\n(Não escreva nenhuma definição. Apenas LISTE as palavras)"
    resposta_palavras_relacionadas = assistant.model.generate_content(prompt_palavras_relacionadas)
    return resposta_palavras_relacionadas.text