import threading
import time

total = 0

def PrintHello(tid):
	global	total
	global	mutex
	mutex.acquire ()
	subtotal = total
	for i in range (50):
		subtotal += i
	time.sleep (tid)
	total = subtotal
	mutex.release ()



threads = []
mutex = threading.Lock()
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append (threading.Thread(target=PrintHello,args=(i,)))
	threads[-1].start()

for i in range (5):
	print ("Aguardando thread "+str(i))
	threads[i].join ()

print ("O total final é: "+str(total))
