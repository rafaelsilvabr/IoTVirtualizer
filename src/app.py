from flask import Flask, request, jsonify, render_template
from flask.wrappers import Response
from manager import Manager
from cataloguer import Cataloguer


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/resources', methods =['GET', 'POST', 'DELETE'])
def receiver():
    if request.method == 'GET':
        # Consulta Resources
        headers = ("id","uuid","description","capabilities","timestamp")
        resources = cataloguer.consultResource()
        return render_template("table.html", headings=headers, data=resources)
    if request.method == 'POST':
        # Cadastro novo Virtual Resource
        try:
            data = request.get_json()
            response = manager.manageRegistResource(data)
            return jsonify(response.__dict__["__data__"])
        except:
            return "[Receiver] Erro no processo de cadastro de um novo Recurso Virtual\n"

@app.route('/capabilities', methods =['GET', 'POST', 'DELETE'])
def capabilities():
    if request.method == 'GET':
        #Consulta Cpabilities
        headers = ("id","name","description","association")
        capabilities = cataloguer.consultCapabilities()
        return render_template("table.html", headings=headers, data=capabilities)
    if request.method == 'POST':
        #Cadastro nova Capability
        try:
            data = request.get_json()
            response = manager.manageRegistCapability(data)
            print(response.__dict__)
            return jsonify(response.__dict__["__data__"])
        except:
            return "Erro no processo de envio\n"

'''
@app.route('/manager', methods=['GET','POST'])
def manager():
    if request.method == 'GET':
        return "Interface de controle de Operações que podem se r realizadas pelo Manager"
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
'''
if __name__ == "__main__":
    manager = Manager()
    cataloguer = Cataloguer() # so pra testar
    app.run(debug=True)


