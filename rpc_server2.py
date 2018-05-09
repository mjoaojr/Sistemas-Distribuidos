from socket import *
import threading
import pickle

APPEND = 1

def atende (conn, cliente):
	try:
		data = conn.recv (4096)
	except Exception:
		return;

	tupla = pickle.loads(data)
	print (tupla)
#	if tupla[0] == APPEND:
	lista = list(tupla[0])
	print (lista)
	dado = int(tupla[1])
	print (dado)
	lista.append (dado)
	print (lista)
	conn.send (pickle.dumps(lista))

	conn.close ()


s = socket ()

host = "10.10.13.1"
porta = 8753
s.bind ((host, porta))
s.listen (10)

while True:
	(conn, cliente) = s.accept ()

	t = threading.Thread(target=atende,args=(conn, cliente, ))
	t.start()
