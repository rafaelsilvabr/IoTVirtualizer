# IoTVirtualizer

<br>
<img src="Virtualizer.png" width="350">
<br>

• Receiver: Implementa a camada responsavel por receber os dados e traduzir as
requisicoes para os metodos internos, pode assumir uma interface REST ou Pub-
Sub;

• Manager: Orquestra as operacoes internas do Virtualizer, e responsavel pelo
fluxo de envio de mensagens e cadastro de novos recursos e operacoes/capabilities
do Virtualizer;

• Catalog: E responsavel pelos dados dos recursos virtuais e definicoes de
operacooes/capabilities que o Virtualizer realiza. Realiza o armazenamento e prove
esses dados aos outros componentes quando requisitado;

• Register: Registra o recurso virtual na plataforma e retorna o uuid de cadastro e caso necessário, (TRABALHO FUTURO) realiza o registro do virtualizer no cadastro dos sensores referenciados pelo recurso virtual em IoTGateways.

• DataProcessor: Responsavel pelo processamento dos dados do recurso virtual. A
cada novo processamento de dados uma instancia nova do componente e criada,
ou seja, cada capabilitie processada resulta na instanciacao de um DataProcessor
diferente, onde o dado e processado. (Ps.: Para esse componente, preciso realizar
um teste na InterSCity para avaliar se essa proposta de funcionamento e viavel,
visto que gerariamos uma requisicao por Capabilitie a plataforma);

• Sender: Envia os dados processados a plataforma.

## Definições Virtual Resource e Capability

Virtual Resource:
	- uuid: id de referência para o recurso na INCT;
	- capabilities: Lista de capabilities do recurso. Lembrando que, para que um registro realize uma capability, essa capability deve ser incluida no Virtualizer anteriormente;
	- realSensors: Valores de referencia a sensores reais,previamente cadastrados na INCT, que possibilitam a descoberta desses sensores através do Resource Discoverer (Microsserviço da plataforma INCT).

Capability:
	- name: Nome de referência da capability
	- def: Definição da operação realizada pela capability. [Mais Informações](defCapability.md).



## Data Template: 

### Exemplo dado p/registro recursos virtuais ou capabilities

O registro de um recurso ou capability no Virtualizer precisa seguir um padrão e informar os segunites dados acerca do recurso Virtual:


```python
	'state' = 'Virtual' or 'Capability' 
```

> Virtual: Informa que se refere à um dado de registro de um recurso virtual ao Virtualizer
> Capability: Informa que se refere à um dado de registro de uma capability nova ao Virtualizer


```python
	'regInfos' : {'data': (dados de registro INCT)}
```

> regInfos: 
>Para Virtual Resources: Segue os padrões de dados de registro da plataforma InterSCity, contem os dados necessários para cadastro de um recurso na platafomra.
> Para Capabilities (TRABALHO FUTURO): Segue os [padrões internos de definição de novas capabilities](defCapability.md).


```python
	'realSensors' : {(Parametros dos sensores REAIS vinculados ao recurso virtual)} 
```

> realSensors: Parâmetros que definem os sensores REAIS que serão utilizados pelo recurso virtual para a composição do dado processado. Pode conter uma refência direta dos sensores (uuid do sensor) ou dados referentes aos recursos existentes na plataforma INCT os quais permitam a localização do sensor através do Resource Dscoverer, microsserviço da INCT.

Exemplo:

```python
	# Registro de um novo recurso Virtual
	msg = {'state':'Virtual',
		'regInfos':{
			'data': {
			"description": "A simple virtual sensor",
			"capabilities": [
				"maxTemperature",
				"minTemperature",
				"averageTemperature"
			],
			"status": "active",
			"lat":10,
			"lon":12
			}
		},
		'realSensors':{
			'ids': ['uuid1','uuid2']
		}
	}
```
```python
	# Registro de uma nova Capability
	msg = {'state':'Capability',
		'regInfos':{
		"description": {
			"maxTemperature":"default",
			"minTemperature":"default"
		}
	}
```

### Dado Recebido pelo Virtualizer
```python
	msg = {
		'uuid': 'xxxx-xxxx-xxxx',
		'data':{
			"data": {
				"temperature": 30
			}
		}
	}
```
.