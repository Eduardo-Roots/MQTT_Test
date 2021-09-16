import paho.mqtt.client as mqtt

import PySimpleGUI as sg

layout = [[sg.Text('Inform a temperature: '), ],
          [sg.InputText(key='temp')],
          [sg.Button('Send'), sg.Button('Quit')]
          ]
window = sg.Window("Adjust of Temperature", layout)

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client("TemperatureInternal")
client.connect(broker)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    else:
        randNumber = values['temp']
        client.publish("TemperatureInternal", randNumber)   # topic TemperatureInternal
        print(f'Published {randNumber} in topic TEMPERATURE')

    window.close()
