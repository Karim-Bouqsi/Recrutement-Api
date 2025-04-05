from rest_framework import serializers
from ..models.offre import Offre

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = ['id', 'titre', 'description', 'lieu', 'type_contrat', 'salaire', 'date_publication', 'recruteur']
