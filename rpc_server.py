from socket import *
import threading

APPEND = 1

def atende (conn, cliente):
	try:
		data = conn.recv (4096)
	except Exception:
		return;

	if data[0] == APPEND:
		data[1].append (data[2])
		conn.send (data)

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
