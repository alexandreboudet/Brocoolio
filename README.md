# Brocoolio

> Équipe Brocoolio
> - Alexandre Boudet
> - Julien Douet
> - Thomas Périchet
> - Younes Rafiki

----------------------------------------------------------------------

## Prérequis

Vérifier que vous avez la dernière version de Docker et Docker Compose d'installée sur votre machine : 

    $ docker --version
    Docker version 18.09.1, build 4c52b90

    $ docker-compose --version
    docker-compose version 1.27.4, build 40524192

Si vous n'avez pas Docker et/ou Docker Compose d'installés veuillez suivre ces tutoriels :

### Docker

https://docs.docker.com/engine/install/ubuntu/

### Docker Compose

https://docs.docker.com/compose/install/

----------------------------------------------------------------------

## Lancer Brocoolio localement

Se déplacer dans le dossier où se trouve le `docker-compose.yml`

Ensuite lancer la commande suivante : 
    
    $ sudo docker-compose up --build

Ensuite aller à l'adresse suivante : 
    
http://0.0.0.0:8000/utilisateur/connexion