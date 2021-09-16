import paho.mqtt.client as mqtt
from random import uniform
import time

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client("TemperatureExternal")
client.connect(broker)

while True:
    randNumber = uniform(22.0, 34.5)
    client.publish("TemperatureExternal", randNumber)  # topic TemperatureExternal
    print(f'Published {randNumber} in topic TEMPERATURE')
    time.sleep(5)
