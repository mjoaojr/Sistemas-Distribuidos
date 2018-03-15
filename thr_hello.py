from threading import Thread

def PrintHello(tid):
	for i in range (5):
		print ("Ola Mundo! Sou a thread "+str(tid)+" - "+str(i))



for i in range (5):
	print ("Criando thread "+str(i))
	t = Thread(target=PrintHello,args=(i,))
	t.start()
