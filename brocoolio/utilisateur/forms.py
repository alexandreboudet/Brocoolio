from django import forms
from django.forms import PasswordInput

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', max_length=100)
    mail = forms.EmailField(label='Mail', max_length=100)
    mdp = forms.CharField(label='Mot de passe',widget=PasswordInput())

class ConnexionForm(forms.Form):
    authentification = forms.CharField(label='Pseudo ou mail', max_length=100)
    mdp = forms.CharField(label='Mot de passe',widget=PasswordInput())

class ModificationForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', max_length=100)
    mail = forms.EmailField(label='Mail', max_length=100)
    mdp = forms.CharField(label='Mot de passe',widget=PasswordInput())
    karma_porteur = forms.BooleanField(required=False)
    karma_financeur = forms.BooleanField(required=False)
    karma_evaluateur = forms.BooleanField(required=False)