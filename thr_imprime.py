import threading

def adif0 ():
	global	semaa
#	print ("semaa = "+str(semaa))
	return semaa != 0

def bdif0 ():
	global	semab
#	print ("semab = "+str(semab))
	return semab != 0

def cdif0 ():
	global	semac
#	print ("semac = "+str(semac))
	return semac != 0

def proca ():
	global	cv, semaa, semab, semac
#	print ("Proca")
	with cv:
		cv.wait_for (adif0)
		semaa = 0
		print ("is ", end="")
		print ("La ", end="")
		semab = 1
		cv.notify_all ()

def procb ():
	global	cv, semaa, semab, semac
#	print ("Procb")
	with cv:
		print ("Sou ", end="")
		semac = 1
		cv.notify_all ()
		semab = 0
		cv.wait_for (bdif0)
		print ("Sal", end="")
		semac = 1
		cv.notify_all ()

def procc ():
	global	cv, semaa, semab, semac
#	print ("Procc")
	with cv:
		cv.wait_for (cdif0)
		semac = 0
		print ("ma", end="")
		semaa = 1
		cv.notify_all ()
		semac = 0
		cv.wait_for (cdif0)
		print ("le", end="")

semaa = semac = 0
semab = 1
cv = threading.Condition()
threads = []
threads.append (threading.Thread(target=proca))
threads.append (threading.Thread(target=procb))
threads.append (threading.Thread(target=procc))
for i in range (3):
	threads[i].start()

for i in range (3):
#	print ("Aguardando thread "+str(i))
	threads[i].join ()

print ()
