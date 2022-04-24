# Établir un connexion USB fiable

Il faut :

1. Créer une connexion USB avec l'ordi
1. Activer un tether (qui crée un Personal Access Network ou l'EV3 est le routeur et l'ordi est le client)
1. Utiliser l'IP fixe du tether - créée par la brique -  pour se connecter.

## 1 - Connexion USB avec l'ordi

1. Sur la brique, aller dans Wireless and Networks > All Network Connections.
1. Connecter le fil USB à l'ordi
1. Cliquer sur la connexion Wired qui apparaît et cocher Connect automatically (ainsi que Connect si c'est la première connexion).

La machine Windows devrait reconnaître un nouvel appareil Carte réseau > Remote NDIS Compatible Device (ouvrir le Gestionnaire des périphériques pour vérifier). 

>Si jamais cette connexion ne s'établit pas correctement, aller dans le Gestionnaire des périphériques, supprimer l'appareil Remote NDIS Compatible Device, débrancher le fil USB et le rebrancher. Cela réinitialisera le pilote pour la connexion.

## 2 - Activer un tether

1. Sur la brique, aller dans Wireless and Networks > Tethering.
1. Cocher Gadget et redémarrer la brique. C'est nécessaire pour activer le changement.
1. Revenir dans Wireless and Networks > Tethering. Gagdet devrait toujours être coché. Si vous aller dans Network Info vous verrez l'adresse IP static 192.168.0.1. C'est ça qu'on utilise (même si une autre adresse IP apparaît en haut de la brique). Bref, la brique sera toujours identifiable avec les paramètres suivants :
    * adresse IP (fixe) : 192.168.0.1
    * nom : robot
    * mot de passe : maker
    
Cette information est utilisé par tous les outils de connexion :
    * *Ev3dev Device Browser* dans VS Code (multi-langue)
    * le plugin *thonny-ev3dev* dans Thonny (Python)
    * *ssh* et *sftp* via la ligne de commande (gestion de la brique et de ses fichiers)

## 3 - Se connecter

Dans tous les cas, il faut que la brique soit déjà connectée avec la configuration des deux étapes précédentes de faites.

### Via une console Command Prompt, PowerShell ou WSL

Pour **lancer une session SSH** (pour lancer des commandes et gérer le système directement sur la brique), taper la commande `ssh robot@192.168.0.1` dans un terminal et entrer le mot de passe "maker". Votre terminal reflète alors le terminal sur la brique.

Pour **lancer une session SFTP** (pour transférer et gérer des fichiers entre la brique et l'ordi), taper la commande `sftp robot@192.168.0.1` dans un terminal et entrer le mot de passe "maker". Votre terminal commence maintenant avec l'invite "sftp> ". 

* Pour de l'aide sur les différentes options du programme sftp, lancer la commande `help`.
* Pour quitter le programme sftp, lancer la commande `exit` ou `quit`.

### Via l'extension "ev3dev device browser" sur VS Code

Pour **vérifier la configuration** de la connexion dans l'extension :

1. Ouvrir Settings avec la combinaison `Ctrl + ,` et taper "ev3".
1. Sous l'option Ev3dev Browser : Additional Devices, cliquer  "Modifier dans settings.json"
1. Voir s'il y a une connexion avec la configuration suivante :
    ```json
        {
            "name": "ev3dev (USB tether)", // ou "ev3dev (wired)"
            "ipAddress": "192.168.0.1"
        },
    ```
1. Si non, ajouter cette configuration à la liste et supprimer les autres (sauf "ev3dev (Bluetooth)").


Pour se connecter, dans l'explorateur, cliquer sur Ev3dev Device Browser et ensuite sur "Click here to connect to a device". Cliquer ensuite sur l'appareil "ev3dev (USB tether)". La connexion devrait s'établir si la brique est connecté via le fil USB.