from django import forms

class CreationProjetForm(forms.Form):
    titre = forms.CharField(label='Titre du projet', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False) 
    photo = forms.ImageField(label='Image du projet',required=False)
    description = forms.CharField(label='Résumé du projet',widget=forms.Textarea(attrs={'class': 'form-control'}),required=False)
    cout_estime = forms.FloatField(label='Coût estimé',widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)

class CommentaireForm(forms.Form):
    commentaire = forms.CharField(label='Commentaire',widget=forms.Textarea(attrs={'class': 'form-control'}),required=False)
