import requests
import json

headers= {
    'Content-type': 'application/json',
}

msg = {'regInfos':{
	    "data": {
	      "description": "A simple virtual sensor",
	      "capabilities": [
	        "maxTemperature",
	        "minTemperature",
	        "averageTemperature"
	      ],
	      "status": "active",
	      "lat":10,
	      "lon":12
	    },
        "realSensors":{

        }
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
"realSensors":["45b7d363-86fd-4f81-8681-663140b318d4",["temperature","pressure"]]
}

msg3 = {
	"name":"capabilitieAleatoria",
	"description":"Max temperature of a region",
	"capability_type":"sensor",
	"association": "$max:temperature" 
}  

response = requests.post ('http://localhost:5000/capabilities', data = json.dumps(msg3),headers=headers)
print(response)
print(response.text)