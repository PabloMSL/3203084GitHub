#Requests es una libreria que se usa para hacer solicitudes http facilmente, en formato json
import requests as rq
respuesta = rq.get("https://api.github.com")
print(respuesta.status_code)
print(respuesta.text)

r = rq.get("https://randomuser.me/api/")
usuario = r.json()
print(usuario)
