import threading
import random
import time

def saldo_negativo():
    return saldo < 0

def func_verifica_saldo():
    global saldo
    while True:
        with sinccond:
            sinccond.wait_for(saldo_negativo)
            if fim:
                break
            print ("Seu saldo está negativo!!")
        time.sleep(1)
    
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
        with sinccond:
            sinccond.notify()
        print("Mais uma operação")
    print("thread morrendo...")

vet=[]
for i in range (100):
    vet.append(random.randint(-500, 500))
#    vet.append(i)
    
saldo = 1000
fim = False

threads=[]
mutex = threading.Lock()
sinccond=threading.Condition()

alerta = threading.Thread (target=func_verifica_saldo)

alerta.start()


for i in range (3):
    print ("Criando thread %d"%(i))
    threads.append(threading.Thread (target=atualiza_saldo))
    threads[-1].start ()


for i in range (3):
    print ("Esperando pela thread %d"%(i))
    threads[i].join()

print ("Saldo final = %.2f"%(saldo))

fim = True
saldo = -1
with sinccond:
    sinccond.notify()

alerta.join()

