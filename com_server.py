from socket import *

s = socket ()

host = "152.92.92.7"
porta = 8752
s.bind ((host, porta))
s.listen (10)

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))

        while True:
                data = conn.recv (4096)

                if not data:
                        break

                print (str(cliente)+" me mandou "+data.decode("utf-8") )

                conn.send (str.encode ("Eu sei que voce me mandou "+data.decode("utf-8") , "UTF-8"))

        print ("Fim da conexao com "+str(cliente))

        conn.close
