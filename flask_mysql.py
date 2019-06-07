import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

@app.route("/cliente/<nome>")
def imprime_cliente (nome=None):
    conn = mysql.connector.connect (host='bdsd2019-1.cnvq5ggzl224.us-east-1.rds.amazonaws.com', user='admin', passwd='AdminSD2019-1', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr = "select * from customers where FirstName=\'"+nome+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret

                                                                                                                            1,1          Topo
app.run(host='0.0.0.0', port='80')

