from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=100)
    free = models.BooleanField()

class Whois(models.Model):
    domains = models.ManyToManyField(Domain)    


domain1 = Domain.objects.create(name="domain1.com", free=None)
domain2 = Domain.objects.create(name="domain2.com", free=None)
whois = Whois.objects.create()
whois.domains.add(domain1, domain2)
print(whois.domains.all())  # Retorna todos os itens associados a este objeto