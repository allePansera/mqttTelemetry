from Auth.MQTTPub import MQTTPub
from Generator.VehicleGenerator import VehicleGenerator
from Generator.TelemetryGenerator import TelemetryGenerator
from datetime import datetime
import json, time


publisher = MQTTPub()
pubSession = publisher.creaSessione()

#genero dei dati casuali da inviare ai subscriber per un topic noto
topic_info = publisher.topic_info
topic_telemtry = publisher.topic_telemetry


#suppongo di avere solo 3 publisher, che sono le mie 3 macchine
vehicleList = []
for i in range(0,3):
    vehicleList.append(VehicleGenerator.generateRandom())
    vehicle = vehicleList[i]
    # pubblico il messaggio retained
    info = pubSession.publish(topic_info.replace("VEHICLE_ID",vehicle.uuid), str(vehicle.__dict__),retain=True)
    info.wait_for_publish()
    print(f'SENT - {datetime.now().strftime("%d/%m%Y %H:%M:%Y")}\t'
          f'Topic: {topic_info.replace("VEHICLE_ID",vehicle.uuid)} '
          f'Payload: {vehicle.__dict__}')

# per tutti i veicoli generati ogni 3 secondi invio delle fine telemtrie
while (1):
    for i in range(0, 3):
        vehicle = vehicleList[i]
        telemetry = TelemetryGenerator.generateRandom()
        info = pubSession.publish(topic_telemtry.replace("VEHICLE_ID",vehicle.uuid), str(telemetry.__dict__))
        info.wait_for_publish()
        print(f'SENT - {datetime.now().strftime("%d/%m%Y %H:%M:%Y")}\t'
              f'Topic: {topic_telemtry.replace("VEHICLE_ID",vehicle.uuid)} '
              f'Payload: {telemetry.__dict__}')
    time.sleep(3)
