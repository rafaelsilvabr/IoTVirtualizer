from database import VirtualRes, Capabilities, ResourceCapability, RealSensors, SensorData
from datetime import datetime
import json

class Cataloguer(object):
    def __init__(self):
        pass

    #realiza cadastro/ponto de acesso dos dados na db
    def consultResource(self):
        try:
            print("[Cataloguer] Consultando Resources")
            resources = VirtualRes.select()
            return resources
        except:
            print("[Cataloguer] Erro no processo de consulta do Resource")
            return -1

    def saveResource(self,data,uuid):
        try:
            #"Registrando o recurso na database"
            res=VirtualRes(
                uuid = uuid["data"]["uuid"],
                description = data["regInfos"]["description"],
                capabilities = data["regInfos"]["capabilities"],
                timestamp = datetime.now()
            )
            #adicionar tratamento capabilities
            print("[Cataloguer] Registrando VirtualResource na DB")
            print(res)
            res.save()
            
            #Realizou a ligação entre Resource - Capability
            for capName in data["regInfos"]["capabilities"]:
                cap = Capabilities.select().where(Capabilities.name == capName)
                capResource = ResourceCapability(
                    capability = cap,
                    virtualresource = res
                )
                capResource.save()
            print("t1")
            #Realiza a ligação entre resource - realSensor
            for realsens in data["realSensors"]:
                try:
                    senuuid = realsens["uuid"]
                except:
                    senuuid = "None"
                try:
                    sencapabilities = realsens["capabilities"]
                except:
                    sencapabilities = "None"
                try:
                    sendescription = realsens["description"]
                except:
                    sendescription = "None"
                print(realsens["capabilities"])
                sen = RealSensors(
                    uuid = senuuid,
                    capabilities = sencapabilities,
                    virtualresource = res,
                    description = sendescription
                )
                sen.save()
            print("t2")
            return res
        except:
            print("[Cataloguer] Erro no salvamento do Recurso")
            return -1
    def consultRealSensors(self):
        try:
            print("[Cataloguer] Consultando realSensors")
            rSensors = RealSensors.select()
            return rSensors
        except:
            print("[Cataloguer] Erro no processo de consulta dos Sensores Reais")
            return -1        

    def consultCapabilities(self):
        try:
            print("[Cataloguer] Consultando Capabilities")
            capabilities = Capabilities.select()
            return capabilities
        except:
            print("[Cataloguer] Erro no processo de consulta da Capability")
            return -1

    def saveCapability(self,data):
        try:
            #"Registrando o recurso na database"
            cap=Capabilities(
                name = data["name"],
                description = data["description"],
                association = data["association"]
            )
            print("[Cataloguer] Registrando nova Capability na DB")
            print(cap)
            cap.save()
            return cap
        except:
            print("[Cataloguer] Erro no salvamento da Capability")
            return -1
            
    def consultData(self):
        try:
            print("[Cataloguer] Consultando Dados")
            data = SensorData.select()
            return data
        except:
            print("[Cataloguer] Erro no processo de consulta dos dados")
            return -1

    def saveData(self,data):
        try:
            #"Registrando o recurso na database"
            sens = RealSensors.select().where(RealSensors.uuid == data["uuid"])
            sensordata=SensorData(
                sensor = sens,
                data = json.dumps(data["data"]),
                timestamp = datetime.now()
            )
            print("[Cataloguer] Registrando nova Dado do Sensor na DB")
            # print(sensordata)
            sensordata.save()
            return sensordata
        except:
            print("[Cataloguer] Erro no salvamento do Dado")
            return -1