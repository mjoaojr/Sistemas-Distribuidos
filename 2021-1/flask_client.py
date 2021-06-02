import requests
import json
import urllib.parse

api = "http://127.0.0.1:8080"
url = api+"/clientes"

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))

for d in dados:
    print (f"{d['CustomerId']} - {d['FirstName']} {d['LastName']}")
    
id = input ("Digite o id desejado: ")

url2 = api+f"/cliente/{id}"

dados = requests.get(url2).json()
#print (json.dumps(dados, indent=4))

if dados[0]['State'] is None:
    print (f"{dados[0]['FirstName']} {dados[0]['LastName']} mora em {dados[0]['Address']}, {dados[0]['City']}, {dados[0]['Country']}")
else:
    print (f"{dados[0]['FirstName']} {dados[0]['LastName']} mora em {dados[0]['Address']}, {dados[0]['City']}, {dados[0]['State']}, {dados[0]['Country']}")
