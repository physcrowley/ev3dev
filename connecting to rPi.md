[Connecting EV3 Brick (EV3dev) and Raspberry Pi via USB (November 11, 2017)](https://noscerevivereest.wordpress.com/2017/11/11/connecting-ev3-brick-ev3dev-and-raspberry-pi-via-usb-november-11-2017/)

...j'ai du faire les parties 3 et 5a avant de faire la partie 2 parce que l'option d'une connexion par fil n'etait pas dans les options reseaux

...ensuite -> utiliser VS Code avec ev3dev browser.

## installer des modules python

il fallait les installer sur le raspberry pi d'abord

le dossier d'installation est `/usr/local/lib/pythonX.Y/dist-packages`

la version de python sur la brique est python3.5

ensuite on utilise la "secure copy protocol" `scp` a partir du raspberry pi pour transferer les modules a ev3dev :
`scp -r /usr/local/lib/pythonX.Y/dist-packages/[module] robot@10.42.0.3:/home/robot/[module]` soit **scp -r [host source ou rien si c'est la machine locale]:[dossier] [host de destination ou rien si c'est elle la machine locale]:[dossier]**

>l'URL du ev3dev (10.42.0.3) sera different si la connexion est par Bluetooth.

il faut d'abord entrer le mot de passe du raspberry pi et ensuite le mot de passe du ev3dev ("maker") pour autoriser le transfert.

finalement, il faut acceder au ev3dev via SSH et transferer le module au bon endroit (on ne peut pas le copier directement dans le dossier systeme avec la commande `scp`) : `mv /home/robot/[module] /usr/local/lib/python3.5/dist-packages/[module]` 
