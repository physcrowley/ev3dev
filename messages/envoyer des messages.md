[Sending and Receiving Messages with MQTT](https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/)

il faut changer l'adresse "localhost" pour le nom du robot (p. ex. "ev3dev")

il faut aussi vraiment s'assurer que mosquitto est lancé (via SSH) avec la commande `systemctl status mosquitto`. Il faut que le service soit "enabled" et "actif"... il se désactive par défaut 5min après le démarrage du système. S'il n'est pas actif, on peut le réactiver avec : `sudo systemctl start mosquitto`.


le délai de transfert de message est considérable dans l'échange publish.py et subscribe.py, alors je crois qu'il faudrait intégrer la connexion des machines au début de leur programme et simplement assurer le suivi de la réception et de l'envoi de messages.
