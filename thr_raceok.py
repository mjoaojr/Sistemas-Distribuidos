import threading
import random
import time

total = 0

def conta ():
	global total, mutex
	
	mutex.acquire ()
	cont = total
	time.sleep (random.randint(0,1))
	total = cont + 1
	mutex.release ()
	
def func_thr ():
	for i in range (10):
		conta ()

threads = []
mutex = threading.Lock ()
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append(threading.Thread(target=func_thr))
	threads[-1].start()

for i in range (5):
	print ("Aguardando thread "+str(i))
	threads[i].join ()

print ("Thread Mae: total = "+str(total))
