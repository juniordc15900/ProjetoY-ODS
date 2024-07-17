from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    preferencias = models.JSONField(default=dict)

class Dominio(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='dominios')
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Sessao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sessoes')
    inicio = models.DateTimeField(auto_now_add=True)

class Clique(models.Model):
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE, related_name='cliques')
    timestamp = models.DateTimeField(auto_now_add=True)
    pagina = models.CharField(max_length=100)
    elemento = models.CharField(max_length=100)
