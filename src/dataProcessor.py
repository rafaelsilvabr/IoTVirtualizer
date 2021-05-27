from primitiveCapabilities import PrimitiveCapabilities

class DataProcessor:
    def __init__(self):
        self.pCapabilities = PrimitiveCapabilities()

    def start(self, data, association):
        response = self.pCapabilities.run(association[0], data)
        print("[DATA PROCESSOR] RESULTADO")
        print(response)
        #defCapavility = capability.association
        #for value in data.dicts()
    
