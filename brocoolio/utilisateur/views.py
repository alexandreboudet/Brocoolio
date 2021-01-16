from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import InscriptionForm,ConnexionForm, ModificationForm
from .models import Utilisateur
from projet.models import Projet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import hashlib

# Create your views here.


def connexion(request):
    if request.method == 'POST':
        connexionform = ConnexionForm(request.POST)

        if connexionform.is_valid():
            authentification = request.POST.get('authentification')
            mdp = request.POST.get('mdp')
            if '@' not in str(authentification):
                user = authenticate(request,username=authentification, password=mdp)
            else:
                user = authenticate(request,email=authentification, password=mdp)
            if user is not None:
                login(request, user)
                print('connexion réussi !')


                return redirect("/projet/accueil")
            else:
                print('connexion pas réussi !')
        else:
            print('formulaire pas valide')
    else:
        connexionform = ConnexionForm()
    connexionform = ConnexionForm(request.POST)

    reponse = {
        'connexionform':connexionform,
    }
    return render(request, 'connexion.html', reponse)

def deconnexion(request):
    logout(request)
<<<<<<< HEAD
    return HttpResponseRedirect("/projet/accueil")
=======
    return redirect(connexion)
>>>>>>> back-younes

def suppression(request):
    id = request.user.id
    u = User.objects.get(id=id)
    testUser = u.delete()
    logout(request)

    return redirect(inscription)

def inscription(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        inscriptionform = InscriptionForm(request.POST)
        # check whether it's valid:
        if inscriptionform.is_valid():
            pseudo = request.POST.get('pseudo')
            mail = request.POST.get('mail')
            mdp = request.POST.get('mdp')
            img_profil = 'brocolie.png'
            user = User.objects.create_user(username=pseudo,email=mail,password=mdp)
            user.save()
            Utilisateur.objects.create(idUser=user,estValide=False,img_profil=img_profil
                                       ,date_creation='1805-02-12',karma_porteur=0,karma_evaluateur=0,karma_financeur=0)
        else:
            print('formulaire pas valide')
    # if a GET (or any other method) we'll create a blank form
    else:
        inscriptionform = InscriptionForm ()

    inscriptionform = InscriptionForm(request.POST)
    reponse = {
        'inscriptionform':inscriptionform,
    }
    return render(request, 'inscription.html', reponse)

def profil(request):
    response = {}
    if request.user.is_authenticated:
        if request.session is not None:
            id = request.user.id
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]
            listProjet = Projet.objects.all().filter(utilisateur_id=id).order_by('-date_creation','titre')
            listProjetCount = listProjet.count()
            
            
            response['listProjet']=listProjet
            response['listProjetCount']=listProjetCount
            response['utilisateur']=utilisateur
        else:
            print('plus de session')
        return render(request, 'profil.html', response)
    else:
        return redirect(connexion)

def editionprofil(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            modificationform = ModificationForm(request.POST)
            # check whether it's valid:
            if modificationform.is_valid():
                pseudo = request.POST.get('pseudo')
                mail = request.POST.get('mail')
                mdp = request.POST.get('mdp')
                user = request.user
                user.username = pseudo
                user.email = mail
                user.set_password(mdp)
                user.save()

            else:
                print('formulaire pas valide')
        # if a GET (or any other method) we'll create a blank form
        else:
            modificationform = ModificationForm ()

        modificationform = ModificationForm(request.POST)
        reponse = {
            'modificationform':modificationform,
        }
        return render(request, 'editionprofil.html', reponse)
    else:
        return redirect(connexion)
<<<<<<< HEAD



def profilprojets(request):
    response = {}
    if request.user.is_authenticated:
        if request.session is not None:
            id = request.user.id
            utilisateur = Utilisateur.objects.all().filter(idUser=id)[0]
            listProjet = Projet.objects.all().filter(utilisateur_id=id).order_by('-date_creation','titre')
            listProjetCount = listProjet.count()
            
            
            response['listProjet']=listProjet
            response['listProjetCount']=listProjetCount
            response['utilisateur']=utilisateur
        else:
            print('plus de session')
        return render(request, 'profilprojets.html', response)
    else:
        return redirect(connexion)
=======
>>>>>>> back-younes
