from rest_framework import generics
from ..models.candidat import Candidat
from ..serializers.candidat import CandidatSerializer

# Possible d'automatiser la création des serializers mais j'opte pour la flexibilité.

class CandidatListCreate(generics.ListCreateAPIView) :
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer


class CandidatDetails(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    lookup_field = 'id'