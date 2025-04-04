from django.db import models
from .recruteur import Recruteur

class Offre(models.Model) :

    contrats = [('CDI', 'CDI'), ('CDD', 'CDD'), ('Stage', 'Stage'), ('Alternance', 'Alternance')]

    titre = models.CharField(max_length=40)
    description = models.TextField()
    lieu = models.CharField(max_length=20)
    type_contrat = models.CharField(max_length=20, choices=contrats)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_publication = models.DateTimeField(auto_now_add=True)
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE, related_name='offres')

    def __str__(self):
        return self.titre
