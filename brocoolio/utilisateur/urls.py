from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('inscription/', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    path('profil',views.profil, name='profil'),
    path('deconnexion',views.deconnexion,name='deconnexion'),
    path('suppression',views.suppression,name='suppression'),
    path('editionprofil',views.editionprofil,name='editionprofil'),
    path('profilprojets',views.profilprojets,name='profilprojets'),
]
