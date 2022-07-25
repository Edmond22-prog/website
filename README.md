# Website

Site web officiel fait avec Html, Bootstrap en Front-End et Django en Back-End

## Pour lancer le site en local, vous devez effectuer les commandes suivantes:

* Vous devez tout d'abord créer un fichier .env dans le repertoire mywebsite du projet, dans lequel vous mettrez l'information suivante:

        SECRET_KEY=ob18$015g(yzdlt3gmx3ksfkybu*4oc(ml#5avw--cg@6m&%n@
* Créer un environnement virtuel, une fois que vous vous retrouvez dans le repertoire du projet

        virtualenv .venv
* Activer cet environnement virtuel

        source .venv/bin/activate
* Installer toutes les dépendances du projet

        pip install -r requirements.txt
Si vous rencontrez des problèmes lors de l'installation des paquets, je vous conseille de supprimer la ligne 11 du fichier requirements.txt et de réessayer...

* Lorsque tout est installé, vous pouvez maintenant lancer le projet

      python manage.py runserver