from socket import  *
import random
import threading
import sys

s = socket ()
servidor="10.10.14.1"
porta=8753
s.connect((servidor, porta))

print ("Conectado ao servidor %s:%d"%(servidor,porta))

jogadas = ["pedra", "papel", "tesoura"]
while True:
	eca = 'eca'
	while eca != '':
		eca = input("Digite ENTER para jogar:")

	jog = random.choice (jogadas)
	print ("Minha jogada é "+jog)

	s.send (str.encode (jog, "UTF-8"))

	resp = s.recv (4096)
	sresp = resp.decode ("UTF-8")
	linhas = sresp.split ("|")

	for ss in linhas:
#		print (ss)
		l = ss.split (":")

		if l[0] == "ERRO":
			print (sresp)
			break

		if l[0] == "OK":
			if (l[1] == "FIM"):
				s.close ()
				exit ()
			print (l[2])
			continue

s.close ()
