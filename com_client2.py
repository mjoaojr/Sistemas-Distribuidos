from socket import  *

s = socket ()

minhastr = "Sistemas distribuidos e facil!!\r\n"
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
print (meusbytes)

s.connect(("152.92.92.7", 8752))
s.send (meusbytes)

data = s.recv (1024)

print (data.decode("utf-8"))

s.close ()
