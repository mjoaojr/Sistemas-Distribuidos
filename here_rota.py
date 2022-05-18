import requests
import urllib.parse
import json

api = "https://geocode.search.hereapi.com/v1/geocode?"
api2 = "https://router.hereapi.com/v8/routes?"
apiKey = "grrcm-ZTC6ge7jLZ5ukPqqY03GtwfBXfqepVHN3s-Gw"

#Rua Gastão Gonçalves, 79, Santa Rosa - Niterói, RJ
#Rua XV de Novembro, 8, Centro - Niterói, RJ

def posicao (str):
    endereco = input (str)

    url = api + urllib.parse.urlencode ({"apiKey":apiKey, "q":endereco})
    print(url)

    dados =requests.get(url).json()
#    print (json.dumps(dados, indent=4))

    lat = dados["items"][0]["position"]["lat"]
    longitude = dados["items"][0]["position"]["lng"]
    
    return lat, longitude

lat1, long1 = posicao ("Qual o endereço de origem? ")
lat2, long2 = posicao ("Qual o endereço de destino? ")

url = api2 + urllib.parse.urlencode ({"apiKey":apiKey, "transportMode":"bicycle", "origin":str(lat1)+","+str(long1), "destination":str(lat2)+","+str(long2), "return":"summary"})
print(url)
dados =requests.get(url).json()
print (json.dumps(dados, indent=4))

tempo = dados["routes"][0]["sections"][0]["summary"]["duration"]
horas = int(tempo / 3600)
minutos = int((tempo - horas * 3600) / 60)
segundos = int(tempo - horas * 3600 - minutos * 60)
print (f'O percurso demora {horas} horas, {minutos} minutos {segundos} segundos')
