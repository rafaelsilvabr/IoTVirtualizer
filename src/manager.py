from datetime import datetime, timedelta
from time import sleep
from sender import Sender
from cataloguer import Cataloguer
from register import Register
from dataProcessor import DataProcessor
from database import VirtualRes, Capabilities, ResourceCapability, RealSensors, SensorData
import json

import csv
import time

class Manager (object):
    def __init__(self):
        print("[MANAGER] MANAGER INICIADO")
        self.sender = Sender()
        self.register = Register()
        self.cataloguer = Cataloguer()
        self.dataProcessor = DataProcessor()

    def manageSendData(self,data):
        print("[MANAGER] Envio de dados Iniciado")
        return self.sender.sendData(data)

    def manageRegistResource(self,data):
        try:     
            response = self.register.regData(data)
            response = json.loads(response)
            #if(response["realSensors"] != None):
            #    self.register.regIoTGateway(data) #cadastra no iot gateway
            if(response != -1):
                resource = self.cataloguer.saveResource(data, response)
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

    def processActivator(self, sleepTime):
        #requisitos satisfeitos?
        processos = ResourceCapability.select()
        i=0
        while(1):
            print("[MANAGER] ProcessActivator Iniciado")
            for rescap in processos:
                ini = time.time()
                cap = Capabilities.select(Capabilities.association, Capabilities.name).where(Capabilities.id==rescap.capability).get()
                cap = cap.__dict__["__data__"]
                association = cap["association"].split(":")
                # print(cap) # jsonCapabilityAssociation

                #rsensors = RealSensors.select().join(VirtualRes).where(VirtualRes == rescap.virtualresource)
                rsensors = RealSensors.select().join(VirtualRes, on=(RealSensors.virtualresource==rescap.virtualresource))
                data = SensorData.select(SensorData.data, SensorData.timestamp).where(SensorData.sensor.in_(rsensors))
                dataList = []
                qtdData = 0
                for value in data.dicts():
                    diference = datetime.now() - value["timestamp"]
                
                    if(diference > timedelta(minutes = 10)):
                        print("[MANAGER] Dado deletado da DB: timestamp > 10 min")
                        querry = SensorData.delete().where(SensorData.timestamp == value["timestamp"])
                        querry.execute()

                for value in data.dicts():
                    qtdData+=1
                    valueData = json.loads(value["data"])
                    dataList.append(valueData[association[1]])
                
                uuid = VirtualRes.select(VirtualRes.uuid).where(VirtualRes.id == rescap.virtualresource)
                for data in uuid.dicts():
                    uuid = data["uuid"]
                print("-------------")
                print(qtdData)
                print("dados encontrados")
                print("-------------")
                if(qtdData>=1):
                    print("[MANAGER] Processando Dado")
                    self.dataProcessor.start(dataList, association, cap["name"], uuid)
                fim = time.time()

                f = open('VIRTUALIZER_time_process_data.csv','a')
                writer = csv.writer(f)
                row = [fim-ini , qtdData, association, datetime.now()]
                writer.writerow(row)
                f.close()

                print("TEMPO PROCESSAMENTO PROCESSACTIVATOR")
                print(fim-ini)
            sleep(sleepTime)
            
            
