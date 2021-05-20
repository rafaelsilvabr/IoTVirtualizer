from sender import Sender
from cataloguer import Cataloguer
from register import Register

class Manager (object):
    def __init__(self):
        print("MANAGER INICIADO")
        self.sender = Sender()
        self.register = Register()
        self.cataloguer = Cataloguer()

    def manageSendData(self,data):
        print("ENTROU NO MANAGER")
        return self.sender.sendData(data)

    def manageRegistResource(self,data):
        try:     
            uuid = self.register.regData(data)
            if(uuid != -1):
                resource = self.cataloguer.saveResource(data, uuid)
                return resource
        except:
            return -1

    def manageRegistCapability(self,data):
        capability={
            "name":data["name"],
            "description":data["description"],
            "capability_type":"sensor"
        }
        response = self.register.regCap(capability)
        if(response != -1):
            capability = self.cataloguer.saveCapability(data)
            return capability
        return -1

    def manageDataProcess(self, data):
        try:
            response = self.cataloguer.saveData(data)
            return response
        except:
            return "[MANAGER] Erro no processo de recebimento de dados"
