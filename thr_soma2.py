from threading import Thread
import time

total = 0

def PrintHello(tid):
	global	total
	subtotal = 0
	for i in range (5):
		subtotal += i
	time.sleep (tid)
	total += subtotal


threads = []
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append (Thread(target=PrintHello,args=(i,)))
	threads[-1].start()

for i in range (5):
	print ("Aguardando thread "+str(i))
	threads[i].join ()

print ("O total final é: "+str(total))
