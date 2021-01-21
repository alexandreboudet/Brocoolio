from django import forms
from django.forms import PasswordInput
from captcha.fields import CaptchaField

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', max_length=100)
    mail = forms.EmailField(label='Mail', max_length=100)
    mdp = forms.CharField(label='Mot de passe',widget=PasswordInput())
    captcha = CaptchaField(label='Est-tu un humain ?')

class ConnexionForm(forms.Form):
    authentification = forms.CharField(label='Pseudo ou mail', max_length=100)
    mdp = forms.CharField(label='Mot de passe',widget=PasswordInput())
    captcha = CaptchaField()

class ModificationForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', max_length=100, required=False)
    mail = forms.EmailField(label='Mail', max_length=100, required=False)
    mdp = forms.CharField(label='Mot de passe',widget=PasswordInput(), required=False)
    karma_porteur = forms.BooleanField(required=False)
    karma_financeur = forms.BooleanField(required=False)
    karma_evaluateur = forms.BooleanField(required=False)
