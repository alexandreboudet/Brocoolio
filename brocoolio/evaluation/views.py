from django.shortcuts import render
from .models import EvaluationProjet
from .forms import EvaluationProjetForm
from projet.models import Projet
from utilisateur.models import Utilisateur
from utilisateur.views import connexion
import datetime

import time


def projet(request,id_projet):
    response = {}
    todaysDate = datetime.date.today()
    projet = Projet.objects.all().filter(id=id_projet)[0]
    print(request.user)

    if (request.method == 'POST')&(request.user.is_authenticated):
        # create a form instance and populate it with data from the request:
        evaluationprojetform = EvaluationProjetForm(request.POST)
        # check whether it's valid:
        if evaluationprojetform.is_valid():
            commentaire = request.POST.get('commentaire')
            idee = request.POST.get('idee')
            impact_social = request.POST.get('impact_social')
            budget = request.POST.get('budget')
            calendrier = request.POST.get('calendrier')

            id = request.user.id
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]
            EvaluationProjet.objects.create(projet=projet,evaluateur=utilisateur,date_evaluation=todaysDate,eval_idee=idee,eval_impact_social=impact_social,eval_calendrier=calendrier,eval_budget=budget,commentaire=commentaire)

            response['succes']='oui'
        else:
            response['succes']='non'
            print('formulaire pas valide')
    # if a GET (or any other method) we'll create a blank form
    elif not request.user.is_authenticated:
        return redirect(connexion)
    else:
        evaluationprojetform = EvaluationProjetForm ()

    evaluationprojetform = EvaluationProjetForm(request.POST)
    response['evaluationprojetform']=evaluationprojetform

    return render(request, 'evaluation.html', response)
