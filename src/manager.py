from sender import Sender
from cataloguer import Cataloguer
from register import Register
from database import VirtualRes, Capabilities, ResourceCapability, RealSensors, SensorData


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

    def processActivator(self):
        #requisitos satisfeitos?
        processos = ResourceCapability.select()
        i=0
        for rescap in processos:
            print(rescap)
            print("-------------------")
            #rsensors = RealSensors.select().join(VirtualRes).where(VirtualRes == rescap.virtualresource)
            rsensors = RealSensors.select().join(VirtualRes, on=(RealSensors.virtualresource==rescap.virtualresource))
            data = SensorData.select(SensorData.data).where(SensorData.sensor.in_(rsensors))
            print(data)
            cap = Capabilities.select(Capabilities.association).where(Capabilities.id==rescap.capability)
            print(cap)
            print("-------------------")

