from threading import *
import time
import random

fila = []
MAX = 10
cheio = Semaphore(MAX)
vazio = Semaphore(MAX)
mutex = Lock()

for i in range(MAX):
    cheio.acquire()

def func_prod():
    global fila
    while True:
        num = random.choice(range(50))
        vazio.acquire()
        with mutex:
            fila.append(num)
            print(str(num) + " produzido, tam = ", len(fila))
        cheio.release()
        time.sleep(random.randint(1,4))

def func_cons():
    global fila
    while True:
        cheio.acquire()
        with mutex:
            num = fila.pop(0)
        vazio.release()
        print (str(num) + " consumido, tam = ", len(fila))
        time.sleep(random.randint(1,5))


produtor = Thread(target=func_prod)
consumidor = Thread(target=func_cons)

produtor.start()
consumidor.start()

produtor.join ()
consumidor.join ()

