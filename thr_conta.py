from threading import Thread

cont = 0

def PrintHello(tid):
	global	cont
	for i in range (10):
		cont += 1
#		print (str(cont))


threads = []
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append (Thread(target=PrintHello,args=(i,)))
	threads[-1].start()

for i in range (5):
	print ("Aguardando thread "+str(i))
	threads[i].join ()


print (str(cont))
