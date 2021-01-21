from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('creation', views.creation, name='creation'),
    path('affichage/<int:id_projet>', views.affichage,name='affichage'),
    path('accueil', views.accueil, name='accueil'),
    path('dernierprojets', views.dernierprojets, name='dernierprojets'),
    path('mieuxevalues', views.mieuxevalues, name='mieuxevalues'),
    path('affichage_eval/<int:id_projet>', views.affichage_eval, name='affichage_eval')
]
