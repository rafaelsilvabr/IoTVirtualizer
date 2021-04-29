from sender import Sender
from cataloguer import Cataloguer
from register import Register

class Manager (object):
    def __init__(self):
        print("MANAGER INICIADO")
        self.sender = Sender()
        self.register = Register()
        self.cataloguer = Cataloguer()

    def manageSendData(self,data):
        print("ENTROU NO MANAGER")
        return self.sender.sendData(data)

    def manageRegistResource(self,data):
        print("ENTROU NO MANAGER")
        uuid = self.register.regData(data)
        if(uuid != -1):
            confirmation = self.cataloguer.registResource(data, uuid)
        return confirmation