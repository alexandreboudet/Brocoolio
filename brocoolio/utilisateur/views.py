from django.shortcuts import render

# Create your views here.


def index(request):
    reponse = {
        'texte':'oui',
    }
    return render(request, 'index2.html', reponse)
