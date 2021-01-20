from django import forms

class EvaluationProjetForm(forms.Form):
    commentaire = forms.CharField(label='Commentaire',widget=forms.Textarea(attrs={'class': 'form-control'}),required=False)
    idee = forms.FloatField(label='Idée',min_value=0.0,max_value=5.0,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)
    impact_social = forms.FloatField(label='Impact social',min_value=0.0,max_value=5.0,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)
    calendrier = forms.FloatField(label='Calendrer',min_value=0.0,max_value=5.0,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)
    budget = forms.FloatField(label='Budget',min_value=0.0,max_value=5.0,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)
