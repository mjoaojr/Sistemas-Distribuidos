from socket import *
import random

s = socket ()

host = "10.10.14.1"
porta = 8753
s.bind ((host, porta))
s.listen (10)

jogadas = ["pedra", "papel", "tesoura"]
placar=[0,0]

(conn, cliente) = s.accept ()
print ("Recebi a conexao de "+str(cliente))

while True:
	data = conn.recv (4096)
	sdata = data.decode("utf-8")

	if (not sdata) or (sdata not in jogadas):
		conn.send (str.encode ("ERRO: Jogada inválida", "UTF-8"))
		continue

	print (str(cliente)+" me mandou "+data.decode("utf-8") )

	minhajog = random.choice (jogadas)

	print (minhajog + " X " + sdata)

	if minhajog == sdata:
		conn.send (str.encode ("OK:EMPATE:Fizemos a mesma jogada.|OK:PLACAR:Eu %d x %d Você."%(placar[0], placar[1]), "UTF-8"))
		continue

	if minhajog == "pedra":
		if sdata == "papel":
			placar[1] += 1
		else:
			placar[0] += 1
	if minhajog == "papel":
		if sdata == "tesoura":
			placar[1] += 1
		else:
			placar[0] += 1
	if minhajog == "tesoura":
		if sdata == "pedra":
			placar[1] += 1
		else:
			placar[0] += 1
	if placar[0] >= 3 or placar[1] >= 3:
		conn.send (str.encode ("OK:JOGADA:O servidor jogou %s.|OK:PLACAR:Servidor %d x %d Você.|OK:FIM"%(minhajog,placar[0], placar[1]), "UTF-8"))
		break
	else:
		conn.send (str.encode ("OK:JOGADA:O servidor jogou %s.|OK:PLACAR:Servidor %d x %d Você."%(minhajog,placar[0], placar[1]), "UTF-8"))


print ("Fim da conexao com "+str(cliente))
conn.close

