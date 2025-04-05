from rest_framework import generics
from ..models.candidature import Candidature
from ..serializers.candidature import CandidatureSerializer

class CandidatureListCreate(generics.ListCreateAPIView) :
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

class CandidatureDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    lookup_field = 'id'
