from django.urls import path
from .views import (CandidatureListCreate, CandidatureDetail, CandidatListCreate, RecruteurListCreate, OffreDetail, OffreListCreate, CandidatDetails, RecruteurDetail)

# urls pour chaque modele
urlpatterns = [
    path('candidats/', CandidatListCreate.as_view(), name='candidats-list-create'),
    path('candidats/<int:id>/', CandidatDetails.as_view(), name="candidat-detail"),

    path('recruteurs/', RecruteurListCreate.as_view(), name='recruteur-list-create'),
    path('recruteurs/<int:id>/', RecruteurDetail.as_view(), name='recruteur-detail'),

    path('offres/', OffreListCreate.as_view(), name='offre-list-create'),
    path('offres/<int:id>/', OffreDetail.as_view(), name='offre-detail'),

    path('candidatures/', CandidatureListCreate.as_view(), name='candidature-list-create'),
    path('candidatures/<int:id>/', CandidatureDetail.as_view(), name='candidature-detail'),
]

