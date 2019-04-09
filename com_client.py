from socket import  *

s = socket ()

#minhastr = "GET /rj/ HTTP/1.1\r\nHost: unilasalle.edu.br\r\nConnection: keep-alive\r\n\r\n"
minhastr = "GET /introducao HTTP/1.1\r\nHost: www.google.com\r\nConnection: keep-alive\r\n\r\n"
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
print (meusbytes)

servidor="unilasalle.edu.br"
porta=80

s.connect((servidor, porta))
s.send (meusbytes)

data = s.recv (4096)

print (data)

s.close ()
