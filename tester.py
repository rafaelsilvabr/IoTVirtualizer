import requests
import json

headers= {
    'Content-type': 'application/json',
}

msg = {'state':'Virtual',
	'registred':False,
	'regInfos':{
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

response = requests.post ('http://localhost:5000/manager', data = json.dumps(msg),headers=headers)
print(response)
print(response.text)