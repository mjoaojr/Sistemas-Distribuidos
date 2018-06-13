import requests
import urllib.parse

nome=input("digite o nome do cliente: ")

api="http://127.0.0.1:5000/cliente/"
url = api+urllib.parse.quote (nome)
print (url)

dados=requests.get(url).json()
print (dados)

