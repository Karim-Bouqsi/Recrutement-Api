# Recrutement-Api

# Installation du projet

1) Clonage du projet

```git clone https://github.com/Karim-Bouqsi/Recrutement-Api```
```cd Recrutement-Api/```

2) Installations de l'environnement

``` pip install -r requirements.txt ```

3) Créer la base de donnée

# Linux : 

```sudo apt install postgresql postgresql-contrib```
```sudo -u postgres psql```

```CREATE DATABASE recrutement;```
```\q```

# Windows : 

Installer postgres si ce n'est pas déjà fait : https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
Après l'installation, lancer le logiciel SQL Shell et tapez la commande :
```CREATE DATABASE recrutement;```

4) Modification du fichier settings.py

Modifier la variable DATABASES pour mettre votre nom d'utilisateur (postgres par defaut) et votre mot de passe choisi lors de l'installation de postgres.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recrutement',
        'USER': 'postgres',
        'PASSWORD': 'ton_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5) Lancer le code

Sur le terminal, tapez ces commandes : 
    - ```cd recrutementApi```
    - ```python manage.py makemigrations```
    - ```python manage.py migrate```
    - ```python manage.py runserver```

Puis accèder à l'api via l'url : `http://127.0.0.1:8000/api`


6) Guide d'utilisations de l'api

Accéder à cette url pour connaitre les différents endpoints disponibles : `http://127.0.0.1:8000/api/schema/swagger-ui/`

7) Les enpoints
 
# Candidats

`/api/candidats/` -> `http://127.0.0.1:8000/api/candidats/`
    - GET : Liste tous les candidats
    - POST : Créer un nouveau candidat

`/api/candidats/<id>/` -> `http://127.0.0.1:8000/api/candidats/{id}`
    - GET : Voir les infos d’un candidat spécifique
    - PUT : Modifier complètement les infos d’un candidat
    - PATCH : Modifier partiellement un candidat
    - DELETE : Supprimer un candidat

# Recruteurs

`/api/recruteurs/` -> `http://127.0.0.1:8000/api/recruteurs/`
    - GET : Liste tous les recruteurs
    - POST : Créer un nouveau recruteur

`/api/recruteurs/<id>/` -> `http://127.0.0.1:8000/api/recruteurs/{id}`
    - GET : Voir les infos d’un recruteur spécifique
    - PUT : Modifier complètement les infos d’un recruteur
    - PATCH : Modifier partiellement un recruteur
    - DELETE : Supprimer un recruteur

# Offres 

`/api/offres/` -> `http://127.0.0.1:8000/api/offres/`
    - GET : Liste toutes les offres
    - POST : Créer une nouvelle offre

`/api/offres/<id>/` -> `http://127.0.0.1:8000/api/offres/{id}`
    - GET : Voir les infos d’une offre spécifique
    - PUT : Modifier complètement les infos d’une offre
    - PATCH : Modifier partiellement une offre
    - DELETE : Supprimer une offre

# Candidature

`/api/candidatures/` -> `http://127.0.0.1:8000/api/candidatures/`
    - GET : Liste toutes les candidatures
    - POST : Créer une nouvelle candidature

`/api/candidatures/<id>/` -> `http://127.0.0.1:8000/api/candidatures/{id}`
    - GET : Voir les infos d’une candidature spécifique
    - PUT : Modifier complètement les infos d’une candidature
    - PATCH : Modifier partiellement une candidature
    - DELETE : Supprimer une candidature

# Documentations

`/api/schema/` -> `http://127.0.0.1:8000/api/schema/`
    - GET : Installation du schéma OpenAI

`/api/schema/swagger-ui/` -> `http://127.0.0.1:8000/api/schema/swagger-ui/`
    - GET : Affiche la doc Swagger