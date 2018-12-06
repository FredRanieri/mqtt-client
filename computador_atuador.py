from mqtt.atuadores import Atuador

ip = "127.0.0.1"
nome = "Comp"
local = "sala"
list_sensor = [('10', '1', 'Umidade'), ('10', '2', 'Luminosidade')]

computador_at = Atuador(ip, nome, local, list_sensor)
computador_at.connect()
computador_at.comeca_seguir()
