#!/usr/bin/env python3

""" Publisher script for messaging from ev3dev.org """

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("ev3crowley",1883,60)
client.publish("topic/test", "Hello world!");
client.disconnect();
