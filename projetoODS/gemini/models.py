from django.db import models
from django.db import models
from googletrans import Translator
from langdetect import detect
import re
import google.generativeai as genai
import nltk
import requests

def arquivo_drive(id_arquivo, caminho_destino):
    URL = "https://drive.usercontent.google.com/download?id=1Db9QSp10KjRwbXMuySoWmsbUoGSKVb8n&export=download&authuser=0&confirm=t&uuid=ceed980d-60f2-4f3f-abc7-51b21ae4d11d&at=APZUnTXl1qyCvh8c0cx2xcnN4M7T:1718650201681"

    with requests.Session() as session:
        response = session.get(URL, params={'id': id_arquivo}, stream=False)
        response.raise_for_status()

        with open(caminho_destino, 'wb') as arquivo:
            for chunk in response.iter_content(chunk_size=32768):
                if chunk:
                    arquivo.write(chunk)

id_arquivo = "1Db9QSp10KjRwbXMuySoWmsbUoGSKVb8n" 
caminho_arquivo = "extensao.txt"
arquivo_drive(id_arquivo, caminho_arquivo)

def carregar_extensoes(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
        extensoes = arquivo.read().splitlines()
    return extensoes

# Create your models here.
class GeminiAssistant:
    def __init__(self):
        genai.configure(api_key="AIzaSyALCWvhhaQgez0kL4NfAL9NWexwRlCTL84")
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.translator = Translator()
        self.extensao_dominio = carregar_extensoes(caminho_arquivo)