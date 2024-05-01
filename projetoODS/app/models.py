from django.db import models
from googletrans import Translator
from langdetect import detect
import re
import google.generativeai as genai
import nltk

nltk.download('wordnet')

class GeminiAssistant:
    def __init__(self):
        genai.configure(api_key="AIzaSyBcdZFc6KxMgZX5C1Tyc_cSUSjarTyLUHI")
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.translator = Translator()

    def iniciar_chat(self, palavras_principais):
        bem_vindo = "##"
        print(len(bem_vindo) * "#")
        print(bem_vindo)

        palavras_relacionadas = self.gerar_palavras_relacionadas(palavras_principais)
        palavras_relacionadas_lista = palavras_relacionadas.split('\n')
        palavras = [p.lower().replace('-', '') for p in palavras_relacionadas_lista if p.strip()]  

        extensoes_br = ["com.br", "net.br", "org.br", "com", "br", "net"]  
        dominios_br = self.gerar_dominios(palavras, extensoes_br)

        print("Domínios Brasileiros:")
        for dominio in dominios_br:
            print(dominio)
        
        print("Encerrando chat!")

    def translate_to_english(self, word):
        translation = self.translator.translate(word, src='pt', dest='en')
        return translation.text

    def translate_to_portuguese(self, words):
        translations = []
        for word in words:
            translation = self.translator.translate(word, src='en', dest='pt')
            translations.append(translation.text)
        return translations

    def gerar_dominios(self, palavras, extensoes):
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

    def gerar_palavras_relacionadas(self, palavras):
        palavras_string = ", ".join(palavras)
        prompt_palavras_relacionadas = f"A partir da lista {palavras_string}, gere uma nova lista para cada item com 10 sinônimos/palavras relacionadas seguindo o seguinte modelo:\n\nPalavra1\nSinônimo1\nSinônimo2\nSinônimo3\nSinônimo4\n...\nSinônimo10\n\nPalavra2\nSinônimo1\nSinônimo2\nSinônimo3\nSinônimo4\n...\nSinônimo10\n\nPalavra3\n...\n\n(Não escreva nenhuma definição. Apenas LISTE as palavras)"
        resposta_palavras_relacionadas = self.model.generate_content(prompt_palavras_relacionadas)
        return resposta_palavras_relacionadas.text

if __name__ == '__main__':
    assistant = GeminiAssistant()
    palavras_principais = ["Floricultura", "Lótus", "Rosas"]
    assistant.iniciar_chat(palavras_principais)
