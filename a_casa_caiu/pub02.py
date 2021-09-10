import paho.mqtt.client as mqtt
from random import uniform
import time

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client("TemperaturaExterna")
client.connect(broker)

while True:
    randNumber = uniform(25.0, 30,0)
    client.publish("TEMPERATURA", randNumber)
    print("Acabado de publicar", (randNumber) "para o tópico TEMPERATURA")
    time.sleep(5)