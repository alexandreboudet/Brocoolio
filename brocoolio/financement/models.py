from django.db import models
from utilisateur.models import Utilisateur
from projet.models import Projet

# Create your models here.

class FinancementProjet(models.Model):
    financeur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE)
    montant = models.FloatField(default=None)
    commentaire = models.TextField()
    date_financement = models.DateField()
