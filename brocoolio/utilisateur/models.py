from django.db import models

# Create your models here.


class Utilisateur(models.Model):
    #id_description = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=30)
    mail = models.CharField(max_length=60)
    mdp_hache = models.CharField(max_length=100)
    estValide = models.BooleanField()
    date_creation = models.DateField()
    karma_porteur = models.IntegerField()
    karma_evaluateur = models.IntegerField()
    karma_financeur = models.IntegerField()
