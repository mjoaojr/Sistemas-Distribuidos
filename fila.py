TAM = 10
buffer = [0]*TAM
ini = fim = 0
nelem = 0
vazios = TAM

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


for i in range (20):
	if not inserir (i):
		print ("Nao consegui inserir "+str(i))
		break
for i in range (20):
	x, y = remover ()
	if x:
		print ("Removi "+str(y))
	else:
		print ("Buffer vazio")
		break
