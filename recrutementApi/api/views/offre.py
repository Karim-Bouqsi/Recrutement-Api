from rest_framework import generics
from ..models.offre import Offre
from ..serializers.offre import OffreSerializer

class OffreListCreate(generics.ListCreateAPIView) :
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

class OffreDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    lookup_field = 'id'
