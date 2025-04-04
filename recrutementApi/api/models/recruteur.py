from django.db import models

class Recruteur(models.Model) :
    
    nom = models.CharField(max_length=15)
    email = models.EmailField()
    entreprise = models.CharField(max_length=30)
    secteur_activite = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    ville = models.CharField(max_length=20)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
