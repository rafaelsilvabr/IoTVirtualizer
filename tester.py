import requests
import json

headers= {
    'Content-type': 'application/json',
}

msg = {
	"uuid":"2021-05-19 20:16:06.280355",
	"data":{
		"temperature": 30,
		"pressure": 1,
		"light": 213
	}
}

msg2 = {
"regInfos":{
	"description": "Recurso Virtual Reguão Norte",
	"capabilities": [
		"maxTemperature",
		"minTemperature",
		"averageTemperature"
	],
	"status": "active",
	"lat":10,
	"lon":12
},
"realSensors":[{"uuid":"45b7d363-86fd-4f81-8681-663140b318d4","capabilities":["temperature","pressure"]}]
}

msg3 = {
	"name":"averageTemperature",
	"description":"Average temperature of a region",
	"capability_type":"sensor",
	"association": "$average:temperature" 
}  

response = requests.post ('http://localhost:5000/data', data = json.dumps(msg),headers=headers)
print(response)
print(response.text)