import paho.mqtt.client as mqtt

import PySimpleGUI as sg

layout = [[sg.Tex('Informe a temperatura: '),],
          [sg.ImputTex(key='temp')],
          [sg.Button('Enviar'), sg.Button('Sair')]
          ]
window = sg.Window("Ajuste de Temperatura", layout)

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client("TemperaturaInterna")
client.connect(broker)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'sair'
        break
    else:
        randNumber = values['temp']
        client.publish("TemperaturaInterna", randNumber)
        print(f'Acabado de publicar {randNumber} para o tópico TEMPERATURA')

    window.close()
