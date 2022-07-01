# Établir un connexion Bluetooth

>🛑 Il ne semble pas y avoir de connexion Bluetooth fiable et stable sur Windows

**La connexion Bluetooth est déconseillée vue son instabilité -> utiliser une connexion par fil USB pour le travail quotidien.**

Mais si vous insistez, il faut :

1. **Créer une connexion Bluetooth** avec l'ordi
1. **Ouvrir la communication** entre la brique et l'ordi.

## 1 - Connexion Bluetooth avec l'ordi

C'est possible d'utiliser la connexion Bluetooth, mais **à chaque connexion avec l'ordinateur l'adresse IP change -> il faut alors changer la configuration de connexion pour l'étape 2 chaque fois aussi**. 

>🛑 La connexion Bluetooth (adresse IP variable) n'est pas aussi pratique que l'adresse IP fixe établi pour la connexion avec un fil USB, et ça ne marche pas chaque fois.

1. Sur la brique, allez dans "Wireless and Networks > Bluetooth".
1. Activez "Powered", ensuite "Visible", ensuite "Start Scan".
1. Naviguez dans la liste, choisir votre ordinateur et cliquer sur "Pair".
1. Suivre les étapes de confirmation sur la brique et sur l'ordi, notamment en :
    * confirmant le code de vérification sur chaque appareil et
    * en acceptant le service AVRCP sur la brique
1. Sur la brique, sortez du menu Bluetooth et allez dans "Wireless and Networks > All Network Connections".
1. Cliquez sur la connexion "[nom de l'ordi]" qui apparaît.
1. Si c'est la première connexion, cliquez sur "Connect". La configuration peut prendre une minute ou deux.
1. Cochez "Connect automatically" pour éviter à refaire ces étapes lors des prochaines connexions.

La machine Windows devrait reconnaître un nouvel appareil. Vous pouvez le vérifier :
* en ouvrant "Paramètres Bluetooth et autres périphériques" sous la liste "Autres appareils" il devrait y avoir un appareil nommé "ev3dev" (ou le nom que vous avez donné à la brique).

## 2 - Établir la communication.

Il faut que la brique soit déjà connectée avec la configuration de l'étape précédente.

### Via VS Code et l'extension "Ev3dev Device Browser"

Pour se connecter, dans l'*Explorateur* :
1. Cliquez sur "Ev3dev Device Browser" et ensuite sur "Click here to connect to a device". 
1. Cliquez ensuite sur l'option "I don't see my device".
    > 🛑 Il faut créer un nouvel appareil chaque fois que la brique est reconnecté à l'ordinateur parce que son adresse IP change et c'est cette adresse qui définit l'appareil.
1. Tapez un nom comme "brique[n]" où `n` est un nouveau nombre comme la date de la connexion.
1. Tapez l'adresse IP que vous voyez en haut de l'écran de la brique.
1. Après quelques (dizaines de) secondes, le cercle jaune deviendra vert indiquant une bonne connexion. 

>Si le cercle devient rouge et il y a un message que la tentative de connexion a pris trop de temps ("timed out"), la connexion a échouée.

Pour **supprimer les vieux appareils** quand la liste devient très longue, suivre les étapes suivantes :

1. Ouvrir Settings avec la combinaison `Ctrl + ,` et taper "ev3dev".
1. Sous l'option *Ev3dev Browser : Additional Devices*, cliquer "Modifier dans settings.json"
1. La liste des appareils sera entre les lignes suivantes :
    ```json
    "ev3devBrowser.additionalDevices": [   
        // liste des appareils ici
    ],
    ```
1. Chaque appareil individuel sera entre accolades comme l'exemple ci-dessous :
    ```json
    {
        "name": "brique 2 fevrier",
        "ipAddress": "169.254.128.182"
    },
    ```
    et l'adresse IP sera différente pour chacun.
1. Supprimez tous les appareils inutiles en sélectionnant d'accolade ouvrante jusqu'à une accolade fermante avec la virgule: `{ ... },`
    >**Ne supprimez pas l'appareil "ev3dev (USB tether)" ou "ev3dev (wired)"** qui est configuré pour la connexion via câble USB.

### Via une console (Command Prompt, PowerShell, Terminal, etc.)

Les options de communication plus avancées via la ligne de commande sont déconseillées à travers la connexion Bluetooth. Établir une connexion avec le fil USB pour utiliser les outils SSH ou SFTP.
