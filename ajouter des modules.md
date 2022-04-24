## installer des modules python sur la brique

1. Utiliser un système Linux (afin d'avoir les versions Linux à transférer sur la brique) :
    * Raspberry Pi
    * WSL... pour installer WSL sur Windows taper les commandes
        ```bash
        wsl --set-default-version 2
        wsl --install -d Ubuntu
        ```
        et entrer votre prénom en minuscules comme nom d'utilisateur ET comme mot de passe¸
1. taper la commande `sudo apt update` et entrer votre mot de passe.
1. taper la commande `sudo apt install python3-pip` pour installer le gestionnaire de packages de python3 (cette commande ne fonctionne pas sans l'étape précédante)
1. obtenir le package voulu, p.ex. paho-mqtt : `pip3 install python3-paho-mqtt`
1. le dossier d'installation est `/usr/local/lib/python3.X/dist-packages`
    * vérifier la version de python avec "python3 --version" et utiliser seulement les 2 premiers chiffres dans le chemin (p.ex. Python 3.8.10 -> python3.8) 
    * la version de python sur la brique est python3.5
    * si on ne trouve pas le module, on peut le chercher avec `pip3 show [package name]`
1. utiliser sftp pour copier le dossier "paho" sur la brique :
    * se connecter avec `sftp robot@[hostname]` où hostname est "ev3dev" par défaut et entrer le mot de passe ("maker" par défaut)
    * cet utilitaire fait le pont entre le dossier local et le dossier à distance (sur la brique). Il rentre dans le dossier /home/robot de la brique.
    * transférer le dossier avec la commande `put /usr/local/lib/python3.X/dist-packages/paho` (changer le chemin au besoin)
    * quitter sftp avec la commande `exit` ou `quit`
1. utiliser ssh pour bouger le dossier au bon endroit sur la brique
    * se connecter avec la commande `ssh robot@[hostname]` où hostname est "ev3dev" par défaut et entrer le mot de passe ("maker" par défaut)
    * vérifier que le dossier du package (p. ex. "paho") est là avec la commande `ls`
    * bouger le dossier avec la commande, p.ex. `sudo mv paho /usr/local/lib/python3.5/dist-packages/paho` pour le package "paho", et entrer le mot de passe. 
    * tester le tout en lançant python interactivement avec la commande `python3`
        * lancer la commande, p.ex. `import paho` (pour le package paho) -> s'il n'y a aucune erreur, l'installation est réussie
        * quitter la session interactive avec la commande `exit()`
    * quitter ssh avec la commande `exit`

