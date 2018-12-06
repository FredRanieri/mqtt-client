from mqtt.atuadores import Sensor
from random import randint
from time import sleep

ip = "127.0.0.1"
porta = 1883
area = '10'
sensor_id = '2'
local = "sala"
tipo = 'Luminosidade'

sensor_humidade = Sensor(ip, porta, area, sensor_id, local, tipo)
sensor_humidade.connect()

print("Sensor Conectado.")

while True:
    msg = str(randint(0,1))
    sensor_humidade.publicar(msg, 0)
    sleep(5)
