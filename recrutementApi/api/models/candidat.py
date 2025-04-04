from django.db import models

class Candidat(models.Model) : 
    
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    date_naissance = models.DateField()
    ville = models.CharField(max_length=15)
    niveau_etude = models.CharField(max_length=15)
    experience = models.TextField()
    competence = models.TextField()

    def __str__(self):
        return self.nom
