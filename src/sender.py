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

        print(uuid)
        print(resourceData)
        response = requests.post (self.inctaddr + '/adaptor/resources/' + uuid + '/data', data = json.dumps(resourceData), headers=self.headers)
        print(response.text)
        print("[SENDER] DADO ENVIADO")
        return response.text