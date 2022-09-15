# FitnessClub 🏆

Dans le cadre d'une évaluation lors de ma formation de développeur web et web mobile, j'ai été amenée à réaliser un dashboard.

## Contexte

FitnessClub est un projet mettant en place la réalisation d'un Dashboard. 
Celui-ci est destiné au staff de la marque afin de gérer les différentes franchises et structure associer à la marque.

Lien du déploiement 👉 https://manouzee.pythonanywhere.com/

## ⚙️ Les fonctionnalités
- Gestions des rôles (admin, staff, franchisé, gérant de structure)
- Gestion des permissions
- Envoyé de Email, lien activation.

- Base de donnée MySQL 
- Déployement sur PythonAnywhere


Les rôles :

Staff -> Simon : email = simon.poiro@gmail.com | password = fitnessclub

Gérant franchise -> Odette : email =  odette.wano@gmail.com  | password = fitnessclub

Gérant structure -> Maurice: email = marice.charlo@gmail.com | password = fitnessclub


## Installation en local

- Cloner le projet :

> git clone  : https://github.com/Manouzze/FitnessClub.git

- Créer un environnement virtuel et l'activer 

> python -m venv .env
> source .env/bin/activate

- Installez les librairies avec pip

> pip install -r requirements.txt

- Ajouter les paramètres de la base de donnés dans le fichier setting.py 
(Django par défaut utilise SQLite, il est donc possible de sauter cette étape si on souhaite SQLite)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '..',
            'USER': '..',
            'PASSWORD': '..',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

- Exécutez les migrations avec le fichier manage.py 

> python manage.py makemigrations
> python manage.py migrate


### Guide de déploiement sur PythonAnywhere

- Cloner le dépôt sur PythonAnywhere dans l'onglet Console

> git clone  : https://github.com/Manouzze/FitnessClub.git

- Créer un environnement virtuel et l'activer 

> python -m venv .env
> source .env/bin/activate

- Installez les librairies avec pip

> pip install -r requirements.txt

- Créer un fichier .env dans le dossier projet

> touch .env

- Utiliser vim pour configurer et ajouter les variables d'environnements dans le fichier .env

> SECRET_KEY=''
> DEBUG=''
> ALLOWED_HOSTS=''

> EMAIL_HOST_USER=""
> EMAIL_HOST_PASSWORD=''

- Ajouter dans l'onglet Web à l'emlacement Virtualenv le chemin du fichier .env

> /home/nom/FitnessClub/.env

- Modification du fichier wsgi : Dans la rublrique Django: 
  1. Ajouter le chemin ou se trouve le fichier manage.py
> path = "/home/nom/FitnessClub/src"
  2. Ajouter le chemin du fichier setting.py
> os.environ['DJANGO_SETTINGS_MODULE'] = 'fitnessClub.settings'

- Créer une base de données MySQL dans l'onglet Database
  1. Configuer dans le fichier setting.py les variables
  DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '..',
            'USER': '..',
            'PASSWORD': '..',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

  2.Effectuer les migrations depuis l'emplacement du fichier manage.py
  > python manage.py makemigrations
  > python manage.py migrate

- Ajouter les chemins des fichiers statics et media dans l'onglet Web 
> URL           Directory
> /static/	/home/nom/FitnessClub/src/static
> /media/	/home/nom/FitnessClub/src/media

- Création du fichier static avec la commande collectstatic
> python manage.py collecstatic

Déploiement Fini ! ✌️
