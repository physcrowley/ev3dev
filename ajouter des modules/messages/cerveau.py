#!/usr/bin/env python3

""" brique centrale """

import paho.mqtt.client as mqtt


client = mqtt.Client()
client.connect("ev3crowley",1883,60) # "ev3dev" est le nom par défaut

running = True

while running :
    msg = input( "Enter any integer or [q] to quit > ")

    # si c'est un nombre entier (+ ou -)
    if (msg[0] == "-" and msg[1:].isdecimal()) or msg.isdecimal() :
        client.publish( "topic/test", msg )
    # si c'est le code pour quitter
    elif msg.lower() == "q" :
        client.publish( "topic/test", msg.lower() )
        # termine la communication
        client.disconnect()
        running = False
    # sinon, pas de communication juste un message d'erreur
    else :
        print("\tinvalid entry")

print("end")
