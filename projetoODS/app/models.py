from django.db import models

class ExemploEntidade(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    class Meta:
        app_label = 'app'