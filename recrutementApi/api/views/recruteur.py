from rest_framework import generics
from ..models.recruteur import Recruteur
from ..serializers.recruteur import RecruteurSerializer

class RecruteurListCreate(generics.ListCreateAPIView) :
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer

class RecruteurDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
    lookup_field = 'id'
