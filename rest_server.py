from sqlalchemy import create_engine
from flask import Flask
import json
from flask_jsonpify import jsonify

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

@app.route("/cliente/<nome>")
def imprime_cliente (nome=None):
    db_connect = create_engine('sqlite:///chinook.db')
    conn = db_connect.connect() # connect to database
    qstr = "select * from customers where FirstName=\'"+nome+"\'"
    print (qstr)
    query = conn.execute(qstr) # This line performs query and returns json result
    result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
    ret = query.fetchone()
    print (ret)
    jret = jsonify(result)
    print (jret)
    return jret



#app.add_url_rule("/eca", "end_eca", imprime_eca)
app.run() # inicia o servidor
#app.run(host='0.0.0.0', port='8752')

