import threading
import random
import time

def atualiza_saldo():
    global vet, saldo, mutex

    while True:
        with mutex:
            if len(vet) == 0:
                break
            valorop = vet.pop()
            saldotemp = saldo
            saldotemp += valorop
            time.sleep(random.randint(0,1))
            saldo = saldotemp
            print ("Saldo = %.2f, tam = %d"%(saldo, len(vet)))

vet=[]
for i in range (100):
    vet.append(random.randint(-500, 500))
#    vet.append(i)
    
saldo = 1000

threads=[]
mutex = threading.Lock()

for i in range (3):
    print ("Criando thread %d"%(i))
    threads.append(threading.Thread (target=atualiza_saldo))
    threads[-1].start ()

for i in range (3):
    print ("Esperando pela thread %d"%(i))
    threads[i].join()

print ("Saldo final = %.2f"%(saldo))
