import random
from Model.VeichleDescriptor import VehicleDescriptor


CAR_BRAND = ["TESLA", "BMW", "AUDI"]
CAR_MODEL = {"TESLA":["model s", "model x", "model y"], "BMW": ["IX3", "IX"], "AUDI":["E-TRON"]}
lastUUID = 0
lastDriverID = 0


class VehicleGenerator:
    """La classe generare dei finiti dispositivi"""
    @staticmethod
    def generateRandom():
        global CAR_MODEL, CAR_BRAND, lastUUID, lastDriverID
        # seleziono la marca della macchina
        brand = CAR_BRAND[random.randint(0,len(CAR_BRAND)-1)]
        # seleziono il modello della macchina
        model = CAR_MODEL[brand][random.randint(0,len(CAR_MODEL[brand])-1)]
        # seleziono lastDriverID
        driverId = lastDriverID
        lastDriverID += 1
        # seleziono il lastUUID
        uuid = lastUUID
        lastUUID+=1
        #ritorno la macchina
        return VehicleDescriptor(uuid, brand, model, driverId)