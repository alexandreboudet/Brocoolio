from django.shortcuts import render,redirect
from .models import Projet,Commentaire
from utilisateur.models import Utilisateur
from evaluation.models import EvaluationProjet
from .forms import CreationProjetForm,CommentaireForm
from evaluation.models import EvaluationProjet
from financement.models import FinancementProjet
from datetime import date
from django.db.models import Sum
# Create your views here.

def index(request):
    reponse = {
        'form':form,
    }
    return render(request, 'index.html', reponse)


def creation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        creationprojetform = CreationProjetForm(request.POST,request.FILES)
        # check whether it's valid:
        if creationprojetform.is_valid():

            titre = request.POST.get('titre')
            photo = request.FILES.get('photo')
            description = request.POST.get('description')
            cout_estime = request.POST.get('cout_estime')

            id = request.session['utilisateur_session']
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]

            todayDate = date.today().strftime("%Y-%m-%d")
            if(photo is not None):
                photo.name = utilisateur.idUser.username

            Projet.objects.create(utilisateur=utilisateur,titre=titre,photo=photo,description=description,cout_estime=cout_estime,estValide=False,date_creation=todayDate,date_validation=todayDate)
            return redirect('/projet/accueil')

        else:
            print('formulaire pas valide')
    # if a GET (or any other method) we'll create a blank form
    else:
        creationprojetform = CreationProjetForm ()

    creationprojetform = CreationProjetForm(request.POST)
    reponse = {
        'creationprojetform':creationprojetform,
    }
    return render(request, 'creation.html', reponse)

def affichage(request,id_projet):

    projet = Projet.objects.all().filter(id=id_projet)[0]
    commentaires = Commentaire.objects.all().filter(projet_id=id_projet)

    financement_somme = FinancementProjet.objects.filter(projet_id=id_projet).aggregate(Sum('montant'))
    if financement_somme['montant__sum'] is None:
        financement_somme['montant__sum'] = 0


    if request.user.is_authenticated:
        id = request.session['utilisateur_session']
        evalprojet = EvaluationProjet.objects.all().filter(evaluateur_id=id)

        utilisateur = Utilisateur.objects.all().filter(id=id)[0]
        # si evalprojet is not none, alors c'est que l'utilisateur a déja évaluer le projet
        if (projet.utilisateur.idUser_id == request.session['utilisateur_session']) | (evalprojet.exists() | utilisateur.karma_evaluateur == 0):
            bool_evalprojet = False
        else:
            bool_evalprojet = True

        if(utilisateur.karma_financeur > 0):
            bool_displayFinanceButton = True

        if (evalprojet.exists()):
            bool_displayShowEvalsButton = True
        else:
            bool_displayShowEvalsButton = False

    if request.method == 'POST':
        commentaireform = CommentaireForm(request.POST)
        if commentaireform.is_valid():

            commentaire = request.POST.get('commentaire')



            Commentaire.objects.create(utilisateur=utilisateur,projet=projet,commentaire=commentaire)

        else:
            print('formulaire pas valide')
    else:
        commentaireform = CommentaireForm ()

    commentaireform = CommentaireForm(request.POST)

    response = {
        "projet":projet,
        "commentaireform":commentaireform,
        "commentaires":commentaires,
        "bool_evalprojet":bool_evalprojet,
        "bool_displayShowEvalsButton":bool_displayShowEvalsButton,
        "financement_somme":financement_somme,
    }
    return render(request, 'affichage.html', response)


def accueil(request):
    response = {}



    listProjet = Projet.objects.all().filter(estValide=1).order_by('-date_creation','titre')
    listProjetEval = Projet.objects.all().filter(estValide=1).order_by('-moyenne_evaluation','-date_creation','titre')
    listProjetCount = listProjet.count()
    bool_porteur = False
    utilisateur = 0

    if request.user.is_authenticated:
        id = request.session['utilisateur_session']
        if(len(Utilisateur.objects.all().filter(id=id)) > 0):
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            if(utilisateur.karma_porteur > 0):
                bool_porteur = True



    response['bool_porteur']=bool_porteur
    response['listProjet']=listProjet
    response['listProjetEval']=listProjetEval
    response['listProjetCount']=listProjetCount
    response['utilisateur']=utilisateur
    if request.method == 'POST':
        value = request.POST.get("search")
        if(value != ""):
            return redirect('/projet/recherche/'+value)
    return render(request, 'accueil.html', response)

def dernierprojets(request):
    response = {}
    if request.session is not None:
        id = request.session['utilisateur_session']
        listProjet = Projet.objects.all().filter(estValide=1).order_by('-date_creation','titre')
        listProjetCount = listProjet.count()
        bool_porteur = False


        if(len(Utilisateur.objects.all().filter(id=id)) > 0):
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            if(utilisateur.karma_porteur > 0):
                bool_porteur = True



        response['bool_porteur']=bool_porteur
        response['listProjet']=listProjet
        response['listProjetCount']=listProjetCount
    else:
        print('plus de session')
    return render(request, 'dernierprojets.html', response)

def mieuxevalues(request):
    response = {}
    if request.session is not None:
        id = request.session['utilisateur_session']
        listProjet = Projet.objects.all().filter(estValide=1).order_by('-moyenne_evaluation','-date_creation','titre')
        listProjetCount = listProjet.count()
        bool_porteur = False

        if(len(Utilisateur.objects.all().filter(id=id)) > 0):
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            if(utilisateur.karma_porteur > 0):
                bool_porteur = True


        response['bool_porteur']=bool_porteur
        response['listProjet']=listProjet
        response['listProjetCount']=listProjetCount
    else:
        print('plus de session')
    return render(request, 'mieuxevalues.html', response)

def affichage_eval(request,id_projet) :

    projet = Projet.objects.all().filter(id=id_projet)[0]
    evalprojet = EvaluationProjet.objects.all().filter(projet=projet)
    for eval in evalprojet:
        eval.moyenneindiv = eval.eval_idee + eval.eval_impact_social + eval.eval_calendrier + eval.eval_budget

    response = {
        "projet":projet,
        "evalprojet":evalprojet
    }
    return render(request, 'affichage_eval.html', response)

def recherche(request,search):
    response = {}
    if request.session is not None:
        id = request.session['utilisateur_session']
        listProjet = Projet.objects.all().filter(estValide=1,titre__contains=search).order_by('-moyenne_evaluation','-date_creation','titre')

        response['listProjet']=listProjet
    else:
        print('plus de session')
    return render(request, 'recherche.html', response)
