from threading import Thread
import time

total = 0

def PrintHello(tid):
	global	total
	subtotal = 0
	for i in range (5):
		subtotal += i
	time.sleep (1)
	total += subtotal



for i in range (5):
	print ("Criando thread "+str(i))
	t = Thread(target=PrintHello,args=(i,))
	t.start()

print ("O total final é: "+str(total))
