from django.shortcuts import render
from .models import Projet,Commentaire
from utilisateur.models import Utilisateur
from .forms import CreationProjetForm,CommentaireForm
from datetime import date
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

            id = request.user.id
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]

            todayDate = date.today().strftime("%Y-%m-%d")
            if(photo is not None):
                photo.name = utilisateur.idUser.username
            
            Projet.objects.create(utilisateur=utilisateur,titre=titre,photo="images/projet/test.png",description=description,cout_estime=cout_estime,estValide=False,date_creation=todayDate,date_validation=todayDate)

            
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
    if request.method == 'POST':
        commentaireform = CommentaireForm(request.POST)
        if commentaireform.is_valid():

            commentaire = request.POST.get('commentaire')
            id = request.user.id
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]

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
    }
    return render(request, 'affichage.html', response)


def accueil(request):
    response = {}
    if request.session is not None:
        id = request.user.id
        listProjet = Projet.objects.all().filter(estValide=0).order_by('-date_creation','titre')
        listProjetCount = listProjet.count()
        
        response['listProjet']=listProjet
        response['listProjetCount']=listProjetCount
    else:
        print('plus de session')
    return render(request, 'accueil.html', response)

def dernierprojets(request):
    response = {}
    if request.session is not None:
        id = request.user.id
        listProjet = Projet.objects.all().filter(estValide=0).order_by('-date_creation','titre')
        listProjetCount = listProjet.count()
        
        response['listProjet']=listProjet
        response['listProjetCount']=listProjetCount
    else:
        print('plus de session')
    return render(request, 'dernierprojets.html', response)

def mieuxevalues(request):
    response = {}
    if request.session is not None:
        id = request.user.id
        listProjet = Projet.objects.all().filter(estValide=0).order_by('-date_creation','titre')
        listProjetCount = listProjet.count()
        
        response['listProjet']=listProjet
        response['listProjetCount']=listProjetCount
    else:
        print('plus de session')
    return render(request, 'mieuxevalues.html', response)