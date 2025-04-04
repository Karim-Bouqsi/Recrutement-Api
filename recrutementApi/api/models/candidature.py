from django.db import models
from .candidat import Candidat
from .offre import Offre

class Candidature(models.Model) : 
    statuts = [('En attente', 'En attente'), ('Accepté', 'Accepté'), ('Refusé', 'Refusé')]
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_name='candidatures')
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name='candidatures')
    date_candidature = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=statuts, default='En attente')

    def __str__(self):
        return self.candidat