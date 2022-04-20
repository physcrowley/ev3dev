#!/usr/bin/env python3

""" Subscriber script from ev3dev.org """

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("10.42.0.1",1883,60) #connection is refused

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()