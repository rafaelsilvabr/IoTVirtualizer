import requests

class Register(object):
    def __init__(self):
        self.headers = {'Content-type': 'application/json'}
        pass
    def regData(self,regInfos):
        print("REGISTRANDO RECURSO VIRTUAL NA INCT")
        msg = 0
        try:
            response = requests.post ('http://addressINCT:8000/adaptor/resources', data = json.dumps(regInfos), headers=self.headers)
            msg = response.text
        except:
            print("[REGISTER]Erro no Registro")
            msg = -1

        return msg