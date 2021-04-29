from flask import Flask, request, jsonify
from manager import Manager

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/receiver', methods =['GET', 'POST', 'DELETE'])
def receiver():
    if request.method == 'GET':
        return "Printa todos comandos para envio"
    if request.method == 'POST':
        #envio novo dado de sensor
        try:
            data = request.get_json()
            return jsonify(manager.manageSendData(data))
        except:
            return "Erro no processo de envio\n"

@app.route('/manager', methods=['GET','POST'])
def manager():
    if request.method == 'GET':
        return "Interface de controle de Operações que podem ser realizadas pelo Manager"
    if request.method == 'POST':
        #requisicao novo (recurso virtual)/(operacao)
        print("METODO DE REGISTRO DE DADO INICIADO")
        try:
            data = request.get_json()
            if(data["state"]=="Virtual"):
                print("DADO VIRTUAL")
                #registrar novo recurso virtual
                response = manager.manageRegistResource(data)
        except:
            response = jsonify({"Data":"Erro no Registro"})
        return response

if __name__ == "__main__":
    manager = Manager()
    app.run(debug=True)


