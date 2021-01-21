from django.shortcuts import render,redirect
from .models import EvaluationProjet
from .forms import EvaluationProjetForm
from projet.models import Projet
from utilisateur.models import Utilisateur
from utilisateur.views import connexion
from django.http import Http404
import datetime

import time


def projet(request,id_projet):
    response = {}
    todaysDate = datetime.date.today()
    projet = Projet.objects.all().filter(id=id_projet)[0]
    if not projet:
        raise Http404("Le projet n'existe pas "+str(id_projet))

    if(projet.utilisateur_id == request.session['utilisateur_session']):
        raise Http404("Vous ne pouvez pas évaluer votre propre projet "+str(id_projet))

    dejaeval = EvaluationProjet.objects.all().filter(evaluateur_id=request.session['utilisateur_session'])
    if dejaeval is not None:
        raise Http404("Vous avez déja évaluer ce projet")

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

            id = request.session['utilisateur_session']
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            EvaluationProjet.objects.create(projet=projet,evaluateur=utilisateur,date_evaluation=todaysDate,eval_idee=idee,eval_impact_social=impact_social,eval_calendrier=calendrier,eval_budget=budget,commentaire=commentaire)
            projet.moyenne_evaluation=(projet.moyenne_evaluation*projet.nbr_evaluation+(float(idee)+float(impact_social)+float(budget)+float(calendrier)))/(projet.nbr_evaluation+1)
            projet.nbr_evaluation = projet.nbr_evaluation + 1

            projet.save()
            if((projet.nbr_evaluation>=2) & (projet.moyenne_evaluation>=10)):
                projet.estValide = True
                projet.save()

            return redirect('/projet/affichage/'+ str(id_projet))


        else:
            print('formulaire pas valide')
    # if a GET (or any other method) we'll create a blank form
    elif not request.user.is_authenticated:
        return redirect(connexion)
    else:
        evaluationprojetform = EvaluationProjetForm ()

    evaluationprojetform = EvaluationProjetForm(request.POST)
    response['evaluationprojetform']=evaluationprojetform

    return render(request, 'evaluation.html', response)

def listeEvaluationProjet(request,id_projet):
    response = {}
    listeEvaluationProjet=EvaluationProjet.objects.all().filter(projet_id=id_projet)

    response['listeEvaluationProjet']=listeEvaluationProjet
    return render(request,'listeEvaluationProjet.html',response)

def listeProjetAEvaluer(request):
    response = {}
    if request.session is not None:
        id = request.session['utilisateur_session']
        listProjet = Projet.objects.all().filter(estValide=0).order_by('-date_creation','titre')

        response['listProjet']=listProjet
    else:
        print('plus de session')
    return render(request, 'listeProjetAEvaluer.html', response)
