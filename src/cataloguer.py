from database import VirtualRes, Capabilities
from datetime import datetime

class Cataloguer(object):
    def __init__(self):
        pass

    #realiza cadastro/ponto de acesso dos dados na db
    def registResource(self,data):
        try:
            print("Registrando o recurso")
            res=VirtualRes(
                uuid = datetime.now(),
                description = data['regInfos']['data']['description'],
                timestamp = datetime.now()
            )
            print(res)
            res.save()
        except:
            print("Erro no REGISTRO")
