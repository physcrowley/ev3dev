# Établir un connexion USB fiable

Il faut :

1. **Activer et configurer un tether** qui crée un Personal Access Network où la brique EV3 est l'hôte et l'ordi est le client
1. **Se brancher avec un fil USB** à l'ordi
1. **Ouvrir la communication** entre la brique et l'ordi.


## 1 - Créer un réseau par USB Tether

1. Sur la brique, allez dans "Wireless and Networks > Tethering".
1. Cochez "Gadget" et redémarrer la brique. C'est nécessaire pour activer le changement.
1. Revenez dans "Wireless and Networks > Tethering".
    * "Gadget" devrait toujours être coché. 
    * Si vous aller dans "Network Info" vous verrez l'adresse IP static 192.168.0.1. C'est ça qu'on utilise (même si une autre adresse IP apparaît en haut de la brique). 
    * Bref, **la brique sera toujours identifiable avec les paramètres suivants** :

    Paramètres du réseau | Valeur
    --- | ---
    hostname (nom de la brique) | ev3dev
    adresse IP (fixe) | 192.168.0.1
    nom du compte | robot
    mot de passe | maker

    Cette information est utilisée par tous les outils de connexion :
    * *Ev3dev Device Browser* dans VS Code
    * *ssh* et *sftp* via la ligne de commande (gestion de la brique et de ses fichiers)
    * le plugin *thonny-ev3dev* dans Thonny (Python)

1. Configuer l'extension "Ev3dev Device Browser" sur VS Code.
    1. Ouvrir Settings avec la combinaison `Ctrl + ,` et taper "ev3dev".
    1. Sous l'option *Ev3dev Browser : Additional Devices*, cliquer "Modifier dans settings.json"
    1. Voir s'il y a une connexion avec la configuration suivante :
        ```json
            {
                "name": "ev3dev (USB tether)", // ou "ev3dev (wired)"
                "ipAddress": "192.168.0.1"
            },
        ```
        * Si non, ajouter cette configuration à la liste.
        * Si oui, mais la valeur pour "ipAddress" n'est pas celle-ci, corriger la valeur.

    >La seule autre connexion devrait être "ev3dev (Bluetooth)" et celle-ci devrait avoir la même ipAddress que "ev3dev (USB tether)" / "ev3dev (wired)". *Supprimer les autres configurations*.

## 2 - Connexion USB avec l'ordi

1. Connectez la brique à l'ordi avec le fil USB.
1. Sur la brique, allez dans *Wireless and Networks > All Network Connections*.
1. Cliquez sur la connexion "Wired" qui apparaît.
1. Si c'est la première connexion, cliquez sur "Connect". La configuration peut prendre une minute ou deux.
1. Cochez "Connect automatically" pour éviter à refaire ces étapes lors des prochaines connexions du fil USB.

La machine Windows devrait reconnaître un nouvel appareil. Vous pouvez le vérifier de deux façons :
* en ouvrant "Paramètres Bluetooth et autres périphériques" sous la liste "Autres appareils" il devrait y avoir un "Remote NDIS Compatible Device" -> c'est l'hôte du réseau (la brique EV3).
* en ouvrant "Gestionnaire des périphériques" sous la rubrique "Cartes réseau" vous devrez aussi voir un "Remote NDIS Compatible Device".

>Si vous ne voyez pas cette connexion, refaire TOUTES les étapes des deux sections précédentes (réseau Tether et connexion avec le fil USB).

## 3 - Établir la communication

Il faut que la brique soit déjà connectée avec la configuration des deux étapes précédentes.

>Si la connexion ne s'établit pas correctement en suivant les étapes ci-dessous, aller dans le "Gestionnaire des périphériques" ou les "Paramètres Bluetooth et autres périphériques", supprimer l'appareil Remote NDIS Compatible Device, débrancher le fil USB et le rebrancher. Cela réinitialisera le pilote pour la connexion.

### Via VS Code et l'extension "Ev3dev Device Browser"

Pour se connecter, dans l'explorateur :
1. Cliquez sur "Ev3dev Device Browser" et ensuite sur "Click here to connect to a device". 
1. Cliquez ensuite sur l'appareil "ev3dev (USB tether)" ou "ev3dev (wired)" que vous avez déjà configuré. 
1. Après quelques (dizaines de) secondes, le cercle jaune deviendra vert indiquant une bonne connexion. 

>Si le cercle devient rouge et il y a un message que la tentative de connexion a pris trop de temps ("timed out"), la connexion a échouée.

### Via une console (Command Prompt, PowerShell, Terminal, etc.)

Voici quelques options plus avancées via la ligne de commande. 

Vous n'avez généralement pas besoin de faire ça pour transférer ou lancer vos programmes, car l'extension VS Code gère tout ça automatiquement.

#### SSH

**Une session SSH** est utile pour lancer des commandes et gérer le système directement sur la brique, p. ex. si vous voulez changer le nom de la brique. 

1. Tapez la commande `ssh robot@192.168.0.1` dans un terminal et 
1. À l'invite `Password: `, entrez le mot de passe "maker". 
    >!!! Les caractères tapés ne s'afficheront pas à la console (le mot de passe est un secret)
1. Votre terminal à l'ordi reflète alors le terminal Linux sur la brique et vous gérer directement le contenu et les paramètres de la brique.

>Si vous avez un message comme `ssh: connect to host ev3dev port 22: Connection timed out`, la connexion a échouée.

#### SFTP

**Une session SFTP** est utile pour transférer et gérer des fichiers entre la brique et l'ordi, p. ex. si vous avez besoin de transférer manuellement des modules MicroPython vers la brique.

1. Tapez la commande `sftp robot@192.168.0.1` dans un terminal et 
1. À l'invite `Password: `, entrez le mot de passe "maker". 
    >!!! Les caractères tapés ne s'afficheront pas à la console (le mot de passe est un secret) 
1. Votre terminal commence maintenant avec l'invite "sftp> ". 
    * Pour de l'aide sur les différentes options du programme sftp, lancer la commande `help`.
    * Pour quitter le programme sftp, lancer la commande `exit` ou `quit`.

>Si vous avez un message comme `ssh: connect to host ev3dev port 22: Connection timed out Connection closed`, la connexion a échouée.
