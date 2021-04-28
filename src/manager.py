from sender import Sender
from cataloguer import Cataloguer

class Manager (object):
    def __init__(self):
        print("MANAGER INICIADO")
        self.sender = Sender()
        self.cataloguer = Cataloguer()

    def manageSendData(self,data):
        print("ENTROU NO MANAGER")
        return self.sender.sendData(data)

    def manageRegistResource(self,data):
        print("ENTROU NO MANAGER")
        return self.cataloguer.registResource(data)