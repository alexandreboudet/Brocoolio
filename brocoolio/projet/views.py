from django.shortcuts import render

# Create your views here.


def index(request):
    reponse = {
        'texte':'weeb',
    }
    return render(request, 'index.html', reponse)
