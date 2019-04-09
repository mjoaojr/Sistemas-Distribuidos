from socket import  *

s = socket ()

minhastr = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
print (meusbytes)

servidor="www.google.com"
porta=80

s.connect((servidor, porta))
s.send (meusbytes)
s.settimeout(1.00)

string = b''
while True:
        try:
                data = s.recv (4096)
        except:
                break
        string += data

print (string)

s.close ()
