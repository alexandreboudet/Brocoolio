from django.db import models
from utilisateur.models import Utilisateur

# Create your models here.

class Projet(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    photo = models.ImageField(null=True,blank=True,upload_to="images/projet/")
    description = models.TextField()
    cout_estime = models.FloatField(default=None)
    estValide = models.BooleanField()
    date_creation = models.DateField()
    date_validation = models.DateField()

class Categorie(models.Model):
    mot_clef = models.CharField(max_length=20)
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE)

class Commentaire(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE)
    commentaire = models.TextField()
