from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('projet/<int:id_projet>', views.projet, name='projet'),
    path('listeEvaluationProjet/<int:id_projet>', views.listeEvaluationProjet, name='listeEvaluationProjet'),
    path('listeProjetAEvaluer', views.listeProjetAEvaluer, name='listeProjetAEvaluer'),
]
