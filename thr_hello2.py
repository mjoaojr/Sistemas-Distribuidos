from threading import Thread

def PrintHello(tid):
	for i in range (5):
		print ("Ola Mundo! Sou a thread "+str(tid))



threads = []
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append (Thread(target=PrintHello,args=(i,)))
	threads[-1].start()

for i in range (5):
	print ("Aguardando thread "+str(i))
	threads[i].join ()
