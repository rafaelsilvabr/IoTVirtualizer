import requests
import json

headers= {
    'Content-type': 'application/json',
}

def cadastrarRecursos():
	msg = {
		"regInfos":{
			"description": "Recurso Virtual Região Norte",
			"capabilities": [
				"averageTemperature",
				"averagePressure"
			],
			"status": "active",
			"lat":10,
			"lon":12
		},
		"realSensors":[{"uuid":"45b7d363-86fd-4f81-8681-663140b318d4","capabilities":["temperature","pressure"]}]
	}

	response = requests.post ('http://localhost:5000/resources', data = json.dumps(msg),headers=headers)
	return response

def cadastrarCapability():
	msg = {
		"name":"averagePressure",
		"description":"Average Pressure of a region",
		"capability_type":"sensor",
		"association": "$average:pressure" 
	}	  
	response = requests.post ('http://localhost:5000/capability', data = json.dumps(msg),headers=headers)
	return response

def sendSensorData():
	msg = {
		"uuid":"2021-06-09 22:25:42.621968",
		"data":{
			"temperature": 10,
			"pressure": 1,
			"light": 213
		}
	}
	response = requests.post ('http://localhost:5000/data', data = json.dumps(msg),headers=headers)
	return response

def testesINCT():
	finaldata={"data": {
		"averagePressure":[{
					"pressure":1.0
				}]
			}
		}
	response = requests.post('http://35.247.228.184:8000/adaptor/resources/' + "0c6573d7-eb51-4688-b2a5-2a4092799b23" + '/data', data = json.dumps(finaldata),headers=headers)
	#response = requests.post ('http://35.247.228.184:8000/catalog/capabilities', data = json.dumps(capability),headers=headers)
	#response = requests.get('http://35.247.228.184:8000/collector/resources/data' ,headers=headers)
	return response

if __name__ == "__main__":
	response = cadastrarRecursos()
	print(response)
	print(response.text)