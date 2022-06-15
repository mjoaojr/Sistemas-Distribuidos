import mysql.connector
from flask import Flask, jsonify, request
from banco import *

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

@app.route("/empregado/<empregado_id>", methods=['GET', 'POST'])
def empregado (empregado_id):
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=porta, database=banco)
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('select * from employees where EmployeeId = ' + empregado_id)  
        records = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        result = [dict(zip(row_headers ,i)) for i in records]
        return jsonify(Erro= False, Messagem= "Successo", Status= 200, Dados = result)

    if request.method == 'POST':
#        print (request.form)
        cursor.execute (f"insert INTO employees (FirstName,LastName,Email) VALUES ('{request.form['FirstName']}','{request.form['LastName']}','{request.form['Email']}')") 
        conn.commit ()
        print(f"Registro {cursor.lastrowid} inserido.")
        return "OK"

@app.route("/vendas_por_ano/<ano>")
def vendas_por_ano (ano=None):
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=porta, database=banco)
    cursor = conn.cursor()
    cursor.execute('select InvoiceId from invoices where YEAR(InvoiceDate)='+ano)  
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(row_headers ,i)) for i in records]
    jret = jsonify(result)
    return jret

@app.route("/valor_por_venda/<id>")
def valor_por_venda (id=None):
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=porta, database=banco)
    cursor = conn.cursor()
    cursor.execute('select Total from invoices where InvoiceId='+id)  
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(row_headers ,i)) for i in records]
    jret = jsonify(result)
    return jret

@app.route("/anos")
def imprime_anos ():
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=porta, database=banco)
    cursor = conn.cursor()
    cursor.execute('select DISTINCT YEAR(InvoiceDate) as ano from invoices')  
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(row_headers ,i)) for i in records]
    jret = jsonify(result)
    return jret

#app.run(host='0.0.0.0', port='80')
app.config['JSON_AS_ASCII'] = False
app.run(host='0.0.0.0', port='8080')