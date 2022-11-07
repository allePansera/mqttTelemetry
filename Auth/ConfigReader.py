import json

class ConfigReader:
    """La classe, fornito un path, ritorno i parametri di configurazione all'interno di un dizionario"""
    @staticmethod
    def read(path):
        with open(path,"r") as jsonStream:
            data = json.load(jsonStream)
            return data