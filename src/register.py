from datetime import datetime
from flask.wrappers import Response
import requests
import json

class Register(object):
    def __init__(self):
        self.headers = {'Content-type': 'application/json'}
        self.inctaddr = open('config.json','r')
        self.inctaddr = json.load(self.inctaddr)
        self.inctaddr = self.inctaddr['inctaddr']
        pass
    def regData(self,regInfos):
        print("[Register] REGISTRANDO RECURSO VIRTUAL NA INCT")
        
        resourceData = {
            'data':regInfos['regInfos']
        }
        try:
            response = requests.post (self.inctaddr + '/adaptor/resources/', data = json.dumps(resourceData), headers=self.headers)
            print(response.text)
            return response.text
        except:
            print("[REGISTER]Erro no Registro")
            return -1
    def regCap(self,regInfos):
        print("[Register] REGISTRANDO CAPABILITY NA INCT")
        try:
            response = requests.post (self.inctaddr + '/catalog/capabilities/', data = json.dumps(regInfos), headers=self.headers)
            print(response.text)
            return response.text
        except:
            print("[REGISTER]Erro no Registro")
            return -1