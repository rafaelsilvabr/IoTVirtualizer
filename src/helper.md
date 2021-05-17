# Porta padrão ocupada

Se o processo não for finalizado da forma correta no terminal (Ctrl + C) a porta padrão continuará sendo ocupada. 

Para finalizar o processo faça
```
$ netstat -tulnp | grep :5000
```

retornará

>tcp 0 0 0.0.0.0:5000 0.0.0.0:* LISTEN xxxx/python3

Então faça
```
$ kill xxxx
```