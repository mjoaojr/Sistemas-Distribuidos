from socket import *
from threading import *
import time

s = socket ()

host = "0.0.0.0"
porta = 8753
s.bind ((host, porta))
s.listen (10)

def horadeimprimir ():
    global cont, flag 
    return (cont % 5 == 0 and flag)

def imprime ():
    global soma, cont, cond, flag
    while True:
        with cond:
            cond.wait_for(horadeimprimir)
            print (f"{soma}")
            flag = False
    

def trata_conn (conn, cliente):
    global soma, cont, cond, flag, mutex
    while True:
        data = conn.recv (4096)

        if not data:
                break

#        print (f"{cliente} me mandou " + data.decode("utf-8") )
    
        with mutex:
            soma += int(data.decode())
        with cond:
            cont += 1
            flag = True
            cond.notify()
            
        conn.send (str.encode ("OK"))

    print ("Fim da conexao com "+str(cliente))
    conn.close()

soma = 0
cont = 0
flag = False

cond = Condition()
mutex = Lock()

Thread(target=imprime).start()

while True:
    (conn, cliente) = s.accept ()
    print (f"Recebi a conexao de {cliente}")

    Thread(target=trata_conn, args=(conn, cliente)).start()
