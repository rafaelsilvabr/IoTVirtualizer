from datetime import datetime
from flask.wrappers import Response
import requests
import json
import urllib.request
import csv
import time

from werkzeug.wrappers import response

class Register(object):
    def __init__(self):
        self.headers = {'Content-type': 'application/json'}
        self.inctaddr = open('config.json','r')
        self.inctaddr = json.load(self.inctaddr)
        self.inctaddr = self.inctaddr['inctaddr']
        pass
    
    def regData(self,regInfos):
        print("[Register] REGISTRANDO RECURSO VIRTUAL NA INCT")
        print(self.inctaddr)
        resourceData = {
            'data':regInfos['regInfos']
        }
        print(resourceData)
        try:
            f = open('VIRTUALIZER_direct_time_regist_resource.csv','a')
            writer = csv.writer(f)
            timeini = time.time()
            data_envio = datetime.now()
            response = requests.post (self.inctaddr + '/adaptor/resources/', data = json.dumps(resourceData), headers=self.headers)
            
            timefim = time.time()
            print("TEMPO DE ENVIO DIRETO")
            print(timefim-timeini)
            
            row = [timefim-timeini , data_envio, json.loads(response.text)["data"]["uuid"]]
            writer.writerow(row)
            f.close()

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

    def regIoTGateway(self,regInfos): #REGISTRO IOTGateway
        # busca inicial apenas pelo uuid
        print("[REGISTER] CADASTRANDO NO IOT GATEWAY")

        for sensor in regInfos["realSensors"]:
            response = requests.get(self.inctaddr + '/catalog/resources/' + sensor["uuid"], headers=self.headers)
            #print(type(response.text))
            # print(response.text)
            iotGatewayAddr = json.loads(response.__dict__["_content"].decode("utf-8"))
            print(iotGatewayAddr["data"]["description"])
            iotGatewayAddr = json.loads(iotGatewayAddr["data"]["description"])
            response = requests.post(iotGatewayAddr["gatewayAddr"] + '/virtualizers', data = urllib.request.urlopen('https://ident.me').read().decode('utf8'), headers = self.headers)