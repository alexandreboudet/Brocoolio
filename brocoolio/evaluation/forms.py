from django import forms

class EvaluationProjetForm(forms.Form):
    commentaire = forms.CharField(label='Commentaire',widget=forms.Textarea)
    idee = forms.FloatField(label='Idée',min_value=0.0,max_value=5.0)
    impact_social = forms.FloatField(label='Impact social',min_value=0.0,max_value=5.0)
    calendrier = forms.FloatField(label='Calendrer',min_value=0.0,max_value=5.0)
    budget = forms.FloatField(label='Budget',min_value=0.0,max_value=5.0)
