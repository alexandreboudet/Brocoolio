from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Utilisateur(models.Model):
    #id_description = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    idUser = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    estValide = models.BooleanField()
    img_profil = models.CharField(max_length=50,default=None)
    date_creation = models.DateField()
    karma_porteur = models.IntegerField()
    karma_evaluateur = models.IntegerField()
    karma_financeur = models.IntegerField()
