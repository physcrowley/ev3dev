# Établir un connexion Bluetooth fiable

>Il ne semble pas avoir une connexion Bluetooth fiable avec Windows

Il faut :

1. Créer une connexion Bluetooth avec l'ordi
1. Activer un tether (qui crée un Personal Access Network ou l'EV3 est le routeur et l'ordi est le client)
1. Utiliser l'IP fixe du tether - créée par la brique -  pour se connecter.

## 1 - Connexion Bluetooth avec l'ordi

1. Sur la brique, aller dans Wireless and Networks > Bluetooth.
1. Activer Powered, ensuite Visible, ensuite Start Scan
1. Naviguer dans la liste, choisir votre ordinateur et cliquer sur Pair.
1. Suivre les étapes de confirmation sur la brique et sur l'ordi.

La machine Windows devrait reconnaître un nouvel appareil Carte réseau > Remote NDIS Compatible Device (ouvrir le Gestionnaire des périphériques pour vérifier). 

>Si jamais cette connexion ne s'établit pas correctement : sur Windows, aller dans les paramètres Bluetooth et autres périphériques et supprimer l'appareil ev3dev sous Autres appareils. Sur la brique, aller dans Wireless and Networks > Bluetooth, cliquer sur l'ordinateur et choisir Remove. Recommencer à la première étape ci-dessus.

## 2 - Activer un tether

>C'est cette partie qui n'est pas fiable... et ça rend la connexion difficile.

1. Sur la brique, aller dans Wireless and Networks > Tethering.
1. Cocher Gadget. Redémarrer la brique; c'est nécessaire pour activer le changement.
1. Revenir dans Wireless and Networks > Tethering. Gagdet devrait toujours être coché.
1. Cocher Bluetooth.
1. Cocher Network Info. Après plusieurs secondes vous verrez l'adresse IP static 192.168.0.1. C'est ça qu'on utilise (même si une autre adresse IP apparaît en haut de la brique). Bref, la brique sera toujours identifiable avec les paramètres suivants :
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
            "name": "ev3dev (Bluetooth)",
            "ipAddress": "192.168.0.1"
        },
    ```
1. Si non, ajouter cette configuration à la liste et supprimer les autres (sauf "ev3dev (wired)" ou "ev3dev (USB tether)").

Pour se connecter, dans l'explorateur, cliquer sur Ev3dev Device Browser et ensuite sur "Click here to connect to a device". Cliquer ensuite sur l'appareil "ev3dev (Bluetooth)". La connexion devrait s'établir si la brique est déjà connecté à l'ordi.