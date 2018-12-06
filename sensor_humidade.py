from mqtt.atuadores import Sensor
from random import randint
from time import sleep

ip = "127.0.0.1"
porta = 1883
area = '10'
sensor_id = '1'
local = "sala"
tipo = 'Umidade'

sensor_umidade = Sensor(ip, porta, area, sensor_id, local, tipo)
sensor_umidade.connect()

print("Sensor Conectado.")

while True:
    msg = str(randint(0,50))
    sensor_umidade.publicar(msg, 0)
    sleep(1)
