import requests
import json

class Sender(object):
    def __init__(self):
        print("SENDER DECLARADO")
        self.headers = {'Content-type': 'application/json'}
        self.inctaddr = open('config.json','r')
        self.inctaddr = json.load(self.inctaddr)
        self.inctaddr = self.inctaddr['inctaddr']
    
    def sendData(self,resourceData, uuid):
        print("SENDER INICIADO")
        response = 0
        try:
            print(uuid)
            print(resourceData)
            response = requests.post (self.inctaddr + '/adaptor/resources/' + uuid + '/data', data = json.dumps(resourceData),headers=self.headers)
            response = "ENVIADO"
            print(response.text)
            #response.text here
            #response = "{}"s
            if(response.text == "{}"):
                return(response.text)
            else:
                return('Response Error')
        except:
            print("[SENDER] Erro no Envio do dado")
            return('Request Error')