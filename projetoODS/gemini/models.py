from django.db import models
from django.db import models
from googletrans import Translator
from langdetect import detect
import re
import google.generativeai as genai
import nltk

# Create your models here.
class GeminiAssistant:
    def __init__(self):
        genai.configure(api_key="AIzaSyBcdZFc6KxMgZX5C1Tyc_cSUSjarTyLUHI")
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.translator = Translator()