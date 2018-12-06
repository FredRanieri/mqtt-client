import paho.mqtt.client as mqtt

class Sensor:
    def __init__(self, ip, porta, area, id, local, tipo):
        self.ip = ip or "127.0.0.1"
        self.porta = porta or 1883
        self.area = area or '0'
        self.id = id or '0'
        self.protocol = mqtt.MQTTv31
        self.local = local or "default"
        self.tipo = tipo or "none"
        self.topic = 'area/' + self.area + '/sensor/' + self.id +'/' + self.tipo

    def connect(self):
        self.client = mqtt.Client(client_id = self.local + str(self.id),
            protocol = mqtt.MQTTv31)

        self.client.connect(self.ip, self.porta)

    def publicar(self, msg, protocol):
        self.client.publish(self.topic, msg, qos = protocol)
        print('Sensor(' + self.area + ', ' + self.id + ') :: -> ' + msg)

class Atuador:
    def __init__(self, ip, nome, local, sensor):
        self.ip = ip or "127.0.0.1"
        self.nome = nome or 'default'
        self.local = local or 'default'
        self.sensor = sensor or []
        self.info = {}

    def connect(self):
        self.client = mqtt.Client(client_id = self.nome + '_' + self.local,
            protocol = mqtt.MQTTv31)

        self.client.connect(self.ip)

    def comeca_seguir(self):
        def on_message(client, userdata, mensagem):
            msg = str(mensagem.payload.decode())
            for s in self.sensor:
                if s[0] in mensagem.topic and s[1] in mensagem.topic and s[2] in mensagem.topic:
                    print(self.nome + ' :: -> ' + 'Sensor(' + s[0] + ', ' + s[1] + ') :: -> ' + msg)
                    aux_info = self.info[s[2]]
                    aux_info.append(msg)
                    if len(aux_info) > 100:
                        del(aux_info[0])
                    self.info[s[2]] = aux_info

        self.client.on_message = on_message
        for s in self.sensor:
            topic = 'area/' + s[0] + '/sensor/' + s[1] + '/' + s[2]
            self.info[s[2]] = []
            self.client.subscribe(topic)

        self.client.loop_forever()
