from threading import Thread

def PrintHello(tid):
	if tid == 0:
		print ("is ", end="")
		print ("La ", end="")
	elif tid == 1:
		print ("Sou ", end="")
		print ("Sal", end="")
	else:
		print ("ma", end="")
		print ("le", end="")



threads = []
for i in range (3):
#	print ("Criando thread "+str(i))
	threads.append (Thread(target=PrintHello,args=(i,)))
	threads[-1].start()

for i in range (3):
#	print ("Aguardando thread "+str(i))
	threads[i].join ()

print ()
