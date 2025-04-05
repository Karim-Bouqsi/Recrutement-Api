from rest_framework import serializers
from ..models import Candidat

class CandidatSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Candidat
        fields = ['id', 'nom', 'prenom', 'email', 'telephone', 'date_naissance', 'ville', 'niveau_etude', 'experience', 'competence']
        