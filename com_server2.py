from socket import *
from threading import Thread

def atende (conn, cliente):
        while True:
                data = conn.recv (4096)

                if not data or len(data) == 0:
                        break

                print (str(cliente)+" me mandou "+data.decode("utf-8") )

                conn.send (str.encode ("Eu sei que voce me mandou "+data.decode("utf-8") , "UTF-8"))

        print ("Fim da conexao com "+str(cliente))

        conn.close
        

s = socket ()

host = "10.10.13.1"
porta = 8752
s.bind ((host, porta))
s.listen (10)
nthr = 0

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()

