import requests

class Sender(object):
    def __init__(self):
        print("SENDER DECLARADO")
        pass
    def sendData(self,data):
        print("SENDER INICIADO")
        try:
            #response = requests.post ('http://34.122.206.9:8000/adaptor/resources/' + dbIds.uuid + '/data', data = json.dumps(p_data),headers=headers)
            #response = "ENVIADO"
            #print(response.text)
            #response.text here
            response = "{}"
            if(response == "{}"):
                return(response)
            else:
                return('Response Error')
        except:
            return('Request Error')