from django import forms

class FinancementProjetForm(forms.Form):
    montant = forms.FloatField(label='Montant',min_value=0.0)
    commentaire = forms.CharField(label='Commentaire',widget=forms.Textarea)
