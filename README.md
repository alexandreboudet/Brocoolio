# Brocoolio

> Rédigé par Alexandre BOUDET  
> Le 11/12/2020

## Environnement virtuel

    $ virtualenv -p python3 venv 
    $ source venv/bin/activate

## Installation des dépendances Python

    $ pip3 install -r requirements.txt

## Base de données

### Installation de Postgresql sur le système

    $ sudo apt install postgresql 


### Démarrage de Postgresql

    $ sudo service postgresql start  

### Connexion à postgresql en tant que superuser

    $ sudo -i -u postgres  

### Entrer dans le prompt psql et on créer un User et une Database

    $ psql  
    postgres=# CREATE USER Brocoolio  
    postgres=# ALTER ROLE Brocoolio WITH CREATEDB;  
    postgres=# CREATE DATABASE Brocoolio OWNER Brocoolio;  
    postgres=# ALTER USER Brocoolio WITH ENCRYPTED PASSWORD 'brocoolio';

### Importation de la Database

    $ psql Brocoolio < db_psql.sql