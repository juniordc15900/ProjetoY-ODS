from django.db import models
import google.generativeai as genai

class GeminiNomeRecomenda:
    def __init__(self):
        API_KEY = "AIzaSyDNg6ZZqDy4SZHEHCEoG5_-Oo2FnAXzxn8"
        genai.configure(api_key = API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')