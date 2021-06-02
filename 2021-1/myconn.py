import mysql.connector

def conecta_chinook():
    host="sd2021-1.cinpbx4dmnin.us-east-1.rds.amazonaws.com"
    port="3306"
    user="admin"
    passwd="SD2021-1"
    database="chinook"
    conn = mysql.connector.connect (host=host, port=port, user=user, passwd=passwd, database=database)
    return conn