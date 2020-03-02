import paho.mqtt.client as mqttclient

import os, csv

'''
Module for collecting sensor data sent over MQTT
'''
def on_connect(client, userdata, flags, rc):
    client.subscribe([("home/door/maindoor"),
                      ("home/door/backdoor"),
                      ("home/window/bedroom"),
                      ("home/window/livingroom"),
                      ("home/window/kitchen")
                      ])

def on_message(client, userdata, msg):
    if(msg.topic == "home/door/maindoor"):
        writeToCsv(1,0, msg.payload.decode())

    if(msg.topic == "home/door/backdoor"):
        writeToCsv(1,1, msg.payload.decode())

    if(msg.topic == "home/window/bedroom"):
        writeToCsv(1,2, msg.payload.decode())

    if(msg.topic == "home/window/livingroom"):
        writeToCsv(1,3, msg.payload.decode())

    if(msg.topic == "home/window/kitchen"):
        writeToCsv(1,4, msg.payload.decode())


def writeToCsv(x,y, payload):
    r = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/doorwindowdata.csv"))
    lines = list(r)
    lines[x][y] = payload
    writer = csv.writer(open(os.path.dirname(__file__)+"/../DataStorage/data/doorwindowdata.csv", 'w'))
    writer.writerows(lines)

def main():
    client = mqttclient.Client("Collector")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost")
    client.loop_forever()

# This below for debugging
if __name__ == "__main__":
    main()