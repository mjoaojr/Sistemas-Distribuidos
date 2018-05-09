from socket import *

APPEND = 1

def append (lista, dado):
	msg = (APPEND, lista, dado)
	s = socket ()
	s.connect(("127.0.0.1", 8752))
	s.send (msg)
	recv = s.recv (4096)
	s.close ()
	return recv

lista = []

for i in range (10):
	lista = append (lista, i)

print (lista)
