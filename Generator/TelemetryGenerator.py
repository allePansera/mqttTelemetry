import random
from Model.GeoLocation import GeoLocation
from Model.ElectricVehicleTelemetry import ElectricVehicleTelemetryData

class TelemetryGenerator:
    """La classe si occupa di generare delle finte telemetrie.
    Viene ritornato un oggetto telemetria"""
    @staticmethod
    def generateRandom():
        # genero la temperatura del motore
        engineTemp = random.randint(50,150)
        # genero la velocità
        speedKmh = random.randint(80,200)
        # genero il livello di carica
        batteryLevel = random.randint(0,100)
        # genero una GeoLocation
        geoLoc = GeoLocation(random.randint(-90,90), random.randint(-180,180), random
                             .randint(0,50))
        # creo l'oggetto da ritornare
        return ElectricVehicleTelemetryData(batteryLevel, geoLoc, speedKmh, engineTemp)