import paho.mqtt.client as mqtt
import time

msg = ''
def on_messagem(client, userdata, message):
    print(f'Message received: {message.payload.decode("utf-8")}')

nome = input("Name of device: ")
broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client(nome)
client.connect(broker)

client.loop_start()
client.subscribe("TemperatureInternal")     # topic publisher01
client.subscribe("TemperatureExternal")     # topic publisher02
client.on_message = on_messagem

time.sleep(120)
client.loop_stop()
