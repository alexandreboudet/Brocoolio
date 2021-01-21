from django.shortcuts import render
from .models import FinancementProjet
from .forms import FinancementProjetForm
from utilisateur.models import Utilisateur
from projet.models import Projet
import datetime

import time
# Create your views here.

def financement(request,idProjet):
    response = {}
    todaysDate = datetime.date.today()
    projet = Projet.objects.all().filter(id=idProjet)[0]
    if not projet:
        raise Http404("Le projet n'existe pas "+str(id_projet))

    if (request.method == 'POST')&(request.user.is_authenticated):
        # create a form instance and populate it with data from the request:


        financementprojet = FinancementProjetForm(request.POST)
        # check whether it's valid:
        if financementprojet.is_valid():
            montant = request.POST.get('montant')
            commentaire = request.POST.get('commentaire')
            date_financement = todaysDate

            id = request.user.id
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]

            FinancementProjet.objects.create(financeur=utilisateur,projet=projet,montant=montant,commentaire=commentaire,date_financement=date_financement)

        else:
            print('formulaire pas valide')
    # if a GET (or any other method) we'll create a blank form
    elif not request.user.is_authenticated:
        return redirect(connexion)
    else:
        financementprojet = FinancementProjetForm ()

    financementprojet = FinancementProjetForm(request.POST)
    response['financementprojet']=financementprojet

    return render(request, 'financement.html', response)