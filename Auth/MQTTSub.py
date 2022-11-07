import paho.mqtt.client as mqtt
from Auth.ConfigReader import ConfigReader
import time


class MQTTSub:
    """La classe gestisce tutti i metodi per il collegamento dei subscriber al broker Mosquito.
    E' definita la variabile che contiene il path per il file di configurazione default.

        Sono definiti e configurati i seguenti metodi di CallBack:
        - on_connect
        - on_disconnect
        - on_message"""

    PATH = "Configurations/Subscriber/config.json"

    @staticmethod
    def onConnect(client, userdata, flags, rc):
        """Il metodo viene usato per gestire la connessione al broker"""
        print(f'Connection status: {rc}')
        topic_info = ConfigReader.read(MQTTSub.PATH)['TOPIC_INFO']
        topic_telemtry = ConfigReader.read(MQTTSub.PATH)['TOPIC_TELEMETRY']
        client.subscribe(topic_info)
        client.subscribe(topic_telemtry)
        print(f'{client.__dict__} subscribed to {topic_info} & {topic_telemtry}')

    @staticmethod
    def onDisconnect(client, userdata, rc):
        if rc != 0:
            print(f'\n{client.__dict__} unexpectedly disconnected from the session. Rc {rc}\n')
        else:
            print(f'\n{client.__dict__} disconnected from the session.\n')

    @staticmethod
    def onMessage(client, userdata, message):
        """Il metodo viene usato per gestire la ricezione dei messaggi dal broker"""
        print("\n##########################################################")
        print(f'Rcv: {message.payload.decode("utf-8")}')
        print(f'Topic: {message.topic}')
        print(f'QoS: {message.qos} Retain Flag: {message.retain}')
        print(f'Client status: {client.__dict__}')
        print("##########################################################\n")

    def __init__(self):
        """Il costruttore accetta i seguenti parametri:
        - PATH (parametro addizionale nel caso in cui non si voglia usare il valore di default).

        L'IP e la porta del broker vengono recuperati dal file di configurazione."""
        self.path = MQTTSub.PATH
        self.username = ConfigReader.read(self.path)['username']
        self.password = ConfigReader.read(self.path)['password']
        self.idClient = ConfigReader.read(self.path)['idClient']
        self.brokerIp = ConfigReader.read(self.path)['broker_ip']
        self.brokerPort = ConfigReader.read(self.path)['broker_port']
        self.topic_info = ConfigReader.read(self.path)['TOPIC_INFO']
        self.topic_telemtry = ConfigReader.read(self.path)['TOPIC_TELEMETRY']

    def creaSessione(self):
        """Il metodo si occupa di creare la sessione mqtt di subscribe per i dati indicati.
        Ritorna un'istanza di mqtt.Client

        L'utilizzatore stabilirà se creare un loop"""
        try:
            client = mqtt.Client(self.idClient)
            client.on_connect = MQTTSub.onConnect
            client.on_disconnect = MQTTSub.onDisconnect
            client.on_message = MQTTSub.onMessage
            client.username_pw_set(self.username,self.password)
            client.connect(self.brokerIp, self.brokerPort)
            return client
        except Exception as e:
            return None