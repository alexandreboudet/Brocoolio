from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import InscriptionForm,ConnexionForm
from .models import Utilisateur
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


                return redirect(profil)
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
    return HttpResponseRedirect("")

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
    if request.session is not None:
        id = request.session.get('_auth_user_id')
        utilisateur = Utilisateur.objects.all().filter(idUser=id)
        response['utilisateur']=utilisateur
    else:
        print('plus de session')
    return render(request, 'profil.html', response)
