from database import VirtualRes, Capabilities
from datetime import datetime

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
            return res
        except:
            print("[Cataloguer] Erro no salvamento do Recurso")
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
            