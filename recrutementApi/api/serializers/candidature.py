from rest_framework import serializers
from ..models.candidature import Candidature

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = ['id', 'candidat', 'offre', 'date_candidature', 'statut']
