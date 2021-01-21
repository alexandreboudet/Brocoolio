from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import InscriptionForm,ConnexionForm, ModificationForm
from .models import Utilisateur
from projet.models import Projet
from evaluation.models import EvaluationProjet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session
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
                utilisateur = Utilisateur.objects.all().filter(idUser=user.id)[0]
                request.session['utilisateur_session']=utilisateur.id
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
    Session.objects.all().delete()
    
    return HttpResponseRedirect("/projet/accueil")

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

def profil(request,id):
    response = {}
    if request.user.is_authenticated:
        if request.session is not None:
            
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            listProjet = Projet.objects.all().filter(utilisateur_id=id).order_by('-date_creation','titre')
            EvaluationCount = EvaluationProjet.objects.all().filter(evaluateur_id=id).count()
            listProjetCount = listProjet.count()

          
            if(request.session['utilisateur_session'] == id):
                bool_myprofile = True
            else:
                bool_myprofile = False
            
            response['EvaluationCount']=EvaluationCount
            response['listProjet']=listProjet
            response['listProjetCount']=listProjetCount
            response['utilisateur']=utilisateur
            response['bool_myprofile']=bool_myprofile
        else:
            print('plus de session')
        return render(request, 'profil.html', response)
    else:
        return redirect(connexion)

def editionprofil(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            id = request.session['utilisateur_session']
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            modificationform = ModificationForm(request.POST)
            # check whether it's valid:
            if modificationform.is_valid():
                pseudo = request.POST.get('pseudo')
                mail = request.POST.get('mail')
                mdp = request.POST.get('mdp')
                karma_porteur = request.POST.get('karma_porteur')
                karma_financeur = request.POST.get('karma_financeur')
                karma_evaluateur = request.POST.get('karma_evaluateur')
                if(karma_porteur and utilisateur.karma_porteur == 0):
                    utilisateur.karma_porteur = 5
                if(karma_financeur and utilisateur.karma_financeur == 0):
                    utilisateur.karma_financeur = 5
                if(karma_evaluateur and utilisateur.karma_evaluateur == 0):
                    utilisateur.karma_evaluateur = 5
                user = request.user
                user.username = pseudo
                user.email = mail
                user.set_password(mdp)
                user.save()
                utilisateur.save()

                return redirect("/utilisateur/connexion")

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



def profilprojets(request):
    response = {}
    if request.user.is_authenticated:
        if request.session is not None:
            id = request.session['utilisateur_session']
            utilisateur = Utilisateur.objects.all().filter(id=id)[0]
            listProjet = Projet.objects.all().filter(utilisateur_id=utilisateur.idUser).order_by('-date_creation','titre')
            EvaluationCount = EvaluationProjet.objects.all().filter(evaluateur_id=utilisateur.idUser).count()
            listProjetCount = listProjet.count()
            
            response['EvaluationCount']=EvaluationCount
            response['listProjet']=listProjet
            response['listProjetCount']=listProjetCount
            response['utilisateur']=utilisateur
        else:
            print('plus de session')
        return render(request, 'profilprojets.html', response)
    else:
        return redirect(connexion)
