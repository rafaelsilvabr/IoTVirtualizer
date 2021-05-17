from datetime import datetime
from flask.wrappers import Response
import requests

class Register(object):
    def __init__(self):
        self.headers = {'Content-type': 'application/json'}
        pass
    def regData(self,regInfos):
        print("[Register] REGISTRANDO RECURSO VIRTUAL NA INCT")
        try:
            #response = requests.post ('http://addressINCT:8000/adaptor/resources', data = json.dumps(regInfos), headers=self.headers)
            #response = response.text
            response = {"data":
                {
                "uuid":datetime.now()
                }
            }
            return response
        except:
            print("[REGISTER]Erro no Registro")
            return -1
    def regCap(self,regInfos):
        print("[Register] REGISTRANDO CAPABILITY NA INCT")
        try:
            #response = requests.post("MANDA PRA INCT")
            #response = response.txt
            response = "Ok"
            return response
        except:
            print("[REGISTER]Erro no Registro")
            return -1