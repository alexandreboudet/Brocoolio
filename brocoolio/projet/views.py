from django.shortcuts import render
from .forms import NameForm
# Create your views here.


def index(request):
    form = NameForm(request.POST)
    print(request.POST.get('your_name'))
    reponse = {
        'form':form,
    }
    return render(request, 'index.html', reponse)
