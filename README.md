# Recrutement-Api

## 1. Clonage du projet

```bash
git clone https://github.com/Karim-Bouqsi/Recrutement-Api
cd Recrutement-Api/
```

## 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

## 3. Création de la base de données

### Linux :

```bash
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql
```

Dans le shell Postgres :
```sql
CREATE DATABASE recrutement;
\q
```

### Windows :

1. Télécharger PostgreSQL : [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
2. Ouvrir SQL Shell (psql) et taper :
```sql
CREATE DATABASE recrutement;
```

## 4. Modifier le fichier `settings.py`

Changer la configuration `DATABASES` :

```python
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
```

## 5. Lancer le serveur

```bash
cd recrutementApi
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Accéder à l'API : [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api)

---

## 6. Documentation Swagger

[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

---

## 7. Liste des Endpoints

### 🔹 Candidats

- `http://127.0.0.1:8000/api/candidats/{id}/`

- `GET /api/candidats/` : Liste des candidats
- `POST /api/candidats/` : Créer un candidat
- `GET /api/candidats/{id}` : Détails d’un candidat
- `PUT /api/candidats/{id}` : Modifier complètement un candidat
- `PATCH /api/candidats/{id}` : Modifier partiellement un candidat
- `DELETE /api/candidats/{id}` : Supprimer un candidat

### 🔹 Recruteurs

- `http://127.0.0.1:8000/api/recruteurs/{id}/`

- `GET /api/recruteurs/` : Liste des recruteurs
- `POST /api/recruteurs/` : Créer un recruteur
- `GET /api/recruteurs/{id}` : Détails d’un recruteur
- `PUT /api/recruteurs/{id}` : Modifier complètement un recruteur
- `PATCH /api/recruteurs/{id}` : Modifier partiellement un recruteur
- `DELETE /api/recruteurs/{id}` : Supprimer un recruteur

### 🔹 Offres

- `http://127.0.0.1:8000/api/offres/{id}/`

- `GET /api/offres/` : Liste des offres
- `POST /api/offres/` : Créer une offre
- `GET /api/offres/{id}` : Détails d’une offre
- `PUT /api/offres/{id}` : Modifier complètement une offre
- `PATCH /api/offres/{id}` : Modifier partiellement une offre
- `DELETE /api/offres/{id}` : Supprimer une offre

### 🔹 Candidatures

- `http://127.0.0.1:8000/api/candidatures/{id}/`

- `GET /api/candidatures/` : Liste des candidatures
- `POST /api/candidatures/` : Créer une candidature
- `GET /api/candidatures/{id}` : Détails d’une candidature
- `PUT /api/candidatures/{id}` : Modifier complètement une candidature
- `PATCH /api/candidatures/{id}` : Modifier partiellement une candidature
- `DELETE /api/candidatures/{id}` : Supprimer une candidature

### 🔹 Documentation

- `GET /api/schema/` : Schéma OpenAPI
- `GET /api/schema/swagger-ui/` : Interface Swagger
