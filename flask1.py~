from flask import Flask

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

@app.route("/") # decorator para rotear a view
def hello_world(): # view
    return "Hello World! <strong>SD com  Flask é mais legal</strong>"

@app.route("/eca")
def imprime_eca ():
    return "Também sei imprimir eca!"

@app.route("/nome/<nome>")
def imprime_nome (nome=None):
    return "Seu nome é "+nome

#app.add_url_rule("/eca", "end_eca", imprime_eca)
app.run() # inicia o servidor
#app.run(host='0.0.0.0', port='8752')
