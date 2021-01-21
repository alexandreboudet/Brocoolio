from django.db import models
from projet.models import Projet
from utilisateur.models import Utilisateur

# Create your models here.

class EvaluationProjet(models.Model):
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE)
    evaluateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    date_evaluation = models.DateField()
    eval_idee = models.FloatField()
    eval_impact_social = models.FloatField()
    eval_calendrier = models.FloatField()
    eval_budget = models.FloatField()
    commentaire = models.TextField()
