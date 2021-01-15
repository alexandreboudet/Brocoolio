from django.shortcuts import render
from .models import Projet,Commentaire
from utilisateur.models import Utilisateur
from .forms import CreationProjetForm,CommentaireForm
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

            id = request.session.get('_auth_user_id')
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]

            photo.name = utilisateur.idUser.username
            Projet.objects.create(utilisateur=utilisateur,titre=titre,photo=photo,description=description,cout_estime=cout_estime,estValide=False,date_creation='1998-12-30',date_validation='2001-06-18')

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
            id = request.session.get('_auth_user_id')
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
