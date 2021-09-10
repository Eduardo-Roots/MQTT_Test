import paho.mqtt.client as mqtt
import time

msg = ''
def on_messagem(client, userdata, message):
    print("Mensagem recebida: ", (message.payload.decode('utf-8'))"")

nome = input("Nome do dispositivo: ")
broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client(nome)
client.connect(broker)

client.loop_start()
client.subscribe("TemperaturaInterna")
client.on_message = on_messagem

time.sleep(120)
client.loop_stop()