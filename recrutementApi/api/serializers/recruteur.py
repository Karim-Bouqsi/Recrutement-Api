from rest_framework import serializers
from ..models.recruteur import Recruteur

class RecruteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruteur
        fields = ['id', 'nom', 'email', 'entreprise', 'secteur_activite', 'telephone', 'ville', 'date_inscription']
