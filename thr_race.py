from threading import Thread
import random
import time

total = 0

def conta ():
	global total
	
	cont = total
	time.sleep (random.randint(0,1))
	total = cont + 1
	
def func_thr ():
	for i in range (10):
		conta ()

threads = []
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append(Thread(target=func_thr))
	threads[-1].start()

for i in range (5):
	print ("Aguardando thread "+str(i))
	threads[i].join ()

print ("Thread Mae: total = "+str(total))
