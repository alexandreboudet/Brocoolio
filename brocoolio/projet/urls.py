from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('creation', views.creation, name='creation'),
    path('affichage/<int:id_projet>', views.affichage,name='affichage'),
]
