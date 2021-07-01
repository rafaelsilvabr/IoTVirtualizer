from primitiveCapabilities import PrimitiveCapabilities
from datetime import datetime
from sender import Sender

class DataProcessor:
    def __init__(self):
        self.pCapabilities = PrimitiveCapabilities()
        self.sender = Sender()

    def start(self, data, association, capName, uuid):
        response = self.pCapabilities.run(association[0], data)
        print("[DATA PROCESSOR] RESULTADO")
        #print(response)

        data = {
            "data":{
                capName:[{
                    association[1]:response/1
                }]   
        }}
        print(data)
        self.sender.sendData(data,uuid)

        

