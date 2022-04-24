#!/usr/bin/env python3

""" briques périphériques """

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  # parce que si c'est du texte, la fonction int() va planter
  try : 
    val = int(msg.payload)
    if val > 0 :
      print("+++")
    elif val < 0 :
      print("---")
    else :
      print("x")
  # et ci ç'a planté, on le traite comme du texte
  except :
    if msg.payload.decode() == "q":
      print("stop")
      client.disconnect()
    else :
      # gérer les cas inattendus
      print(f"msg was : {msg.payload}", end=". ")
      choice = input("keep listening? y/n > ")
      if choice.lower() != "y" :
        client.disconnect()

client = mqtt.Client()
client.connect("192.168.0.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()