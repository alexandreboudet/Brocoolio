from django import forms

class CreationProjetForm(forms.Form):
    titre = forms.CharField(label='Titre du projet', max_length=100)
    photo = forms.ImageField(label='Image du projet')
    description = forms.CharField(label='Résumé du projet',widget=forms.Textarea)
    cout_estime = forms.FloatField(label='Coût estimé')
