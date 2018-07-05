import random
import threading

TAM = 10
buffer = [0]*TAM
ini = fim = 0
nelem = 0
vazios = TAM

cv = threading.Condition()
mutex = threading.Lock ()


def esta_cheio ():
	return nelem == TAM

def esta_vazio ():
	return nelem == 0

def inserir (valor):
	global	fim, buffer, nelem
	if esta_cheio ():
		return False

	buffer[fim] = valor
	fim = (fim + 1)%TAM
	nelem += 1
	return True

def remover ():
	global	ini, buffer, nelem
	if esta_vazio ():
		return False, -1

	valor = buffer[ini]
	ini = (ini + 1)%TAM
	nelem -= 1
	return True, valor

def tem_espaco ():
	print ("nelem = "+str(nelem))
	return nelem < TAM

def produtor ():
	global cv, mutex
	for i in range (40):
		n = random.randrange(100)
		with cv:
			cv.wait_for (tem_espaco)
			with mutex:
				inserir (n)
			print ("Inseri "+str(n))
			cv.notify_all ()

def tem_dado ():
	return nelem > 0

def consumidor ():
	global cv, mutex
	for i in range (40):
		with cv:
			cv.wait_for (tem_dado)
			with mutex:
				eca, n = remover ()
			print ("Removi "+str(n))
			cv.notify_all ()
			


random.seed ()
threads=[]
threads.append(threading.Thread(target=produtor))
threads[-1].start ()
threads.append(threading.Thread(target=consumidor))
threads[-1].start ()

for i in range (2):
        threads[i].join ()

