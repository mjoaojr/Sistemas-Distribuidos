import requests
import urllib.parse
import json

servidor = "http://127.0.0.1:8080/"

def ler_empregado():
    empregado_id = input ("Digite o ID do empregado: ")
    url = servidor+"empregado/"+empregado_id
    dados =requests.get(url).json()
    
    if not dados["Erro"]:
        print (json.dumps(dados["Dados"], indent=4))
        
def print_menu ():
    print ("1 - Ler os dados de um empregado")
    print ("2 - Inserir um empregado")
    print ("9 - Sair")
        
def inserir_empregado ():
    nome = input ("Digite o nome: ")
    sobrenome = input ("Digite o sobrenome: ")
    mail = input ("Digite o email: ")
    url = servidor+"empregado/"+str(0)
    resp = requests.post (url, data = {"FirstName":nome, "LastName":sobrenome, "Email":mail})
    return resp.status_code


while True:
    print_menu ()
    opcao = input ("Digite a opção: ")
    
    if opcao == '1':
        ler_empregado ()
    elif opcao == '2':
        inserir_empregado ()
    elif opcao == '9':
        break
    else:
        print ("Opção inválida")
    

# maior_soma = 0.0
# maior_ano = 0
# for i in dados:
#     url = servidor + "vendas_por_ano/"+str(i['ano'])
#     vendas =requests.get(url).json()
# #    print (json.dumps(dados, indent=4))
# #    print (f"{dados[0]['FirstName']} {dados[0]['LastName']}")
#     soma = 0.0
#     for v in vendas:
#         url = servidor + "valor_por_venda/"+str(v['InvoiceId'])
#         valor =requests.get(url).json()
#         soma += valor[0]['Total']
        
#     if soma > maior_soma:
#         maior_soma = soma
#         maior_ano = i['ano']
        
# print (f"Ano {maior_ano} - {maior_soma:.2f}")
