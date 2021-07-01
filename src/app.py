from flask import Flask, request, jsonify, render_template
from flask.wrappers import Response
from manager import Manager
from cataloguer import Cataloguer

import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resources', methods =['GET', 'POST', 'DELETE'])
def receiver():
    if request.method == 'GET':
        # Consulta Resources
        headers = ("id","uuid","description","capabilities","timestamp")
        resources = cataloguer.consultResource()
        return render_template("table.html", headings=headers, data=resources)
    if request.method == 'POST':
        timeini = time.time()
        # Cadastro novo Virtual Resource
        try:
            data = request.get_json()
            response = manager.manageRegistResource(data)
            timefim = time.time()
            print("TEMPO DE EXECUÇÃO")
            print(timefim-timeini)
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

@app.route('/realsensors', methods=['GET'])
def realsensors():
    if request.method == 'GET':
        headers = ("id", "uuid", "description", "capabilities", "virtualresource")
        realSensors = cataloguer.consultRealSensors()
        return render_template("table.html", headings=headers, data=realSensors) 


@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def data():
    if request.method == 'GET':
        #Consulta Datas
        headers = ("id", "sensor", "data", "timestamp")
        sensorsData = cataloguer.consultData()
        return render_template("table.html", headings=headers, data=sensorsData) 
    if request.method == 'POST':
        try:
            timeini = time.time()
            data = request.get_json()
            response = manager.manageDataProcess(data)
            timefim = time.time()
            print("TEMPO DE EXECUÇÃO: ")
            print(timefim-timeini)
            return jsonify("{}")
        except:
            return "[RECEIVER] Erro no processo de recebimento da dados do sensor"

import threading

if __name__ == "__main__":
    manager = Manager()
    cataloguer = Cataloguer() # so pra testar
    w1 = threading.Thread(target = manager.processActivator, args=(10,))
    
    w1.start()
    app.run(host = "0.0.0.0", port = 8000)

