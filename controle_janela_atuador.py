from mqtt.atuadores import Atuador

ip = "127.0.0.1"
nome = "Janela"
local = "sala"
list_sensor = [('10', '1', 'Umidade')]

janela_at = Atuador(ip, nome, local, list_sensor)
janela_at.connect()
janela_at.comeca_seguir()
