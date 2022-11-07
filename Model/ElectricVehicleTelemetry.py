import json
import random
import time
from Model.GeoLocation import GeoLocation

class ElectricVehicleTelemetryData :

    def __init__(self, batteryLevel, geoLocation, speedKmh, engineTemperature) :
        """Parametri:
        - battery level: float
        - geoLocation: oggetto geoLocation
        - speedKmh: float
        - engineTemperature: float -> si suppone che la misura sia in celsius
        """
        self.batteryLevel = round(batteryLevel,1)
        self.geoLocation = geoLocation.__dict__
        self.speedKmh = round(speedKmh,2)
        self.engineTemperature = round(engineTemperature,2)
        self.timestamp = int ( time . time () )

    def to_json (self):
        return json.dumps(self , default = lambda o : o. __dict__ )
