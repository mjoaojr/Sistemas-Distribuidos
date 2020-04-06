from threading import Thread, Condition
import time
import random

fila = []
MAX = 10
cond = Condition()

def tem_espaco ():
    return len(fila) < MAX

def func_prod():
    global fila
    while True:
        with cond:
            cond.wait_for (tem_espaco)
            num = random.choice(range(50))
            fila.append(num)
            print (str(num) + " produzido, tam = ", len(fila))
            cond.notify()
        time.sleep(random.randint(1,3))

def tem_dado ():
    return len(fila) > 0

def func_cons():
    global fila
    while True:
        with cond:
            cond.wait_for (tem_dado)
            num = fila.pop(0)
            print (str(num) + " consumido, tam = ", len(fila))
            cond.notify()
        time.sleep(random.randint(1,10))


produtor = Thread(target=func_prod)
consumidor = Thread(target=func_cons)

produtor.start()
consumidor.start()

produtor.join ()
consumidor.join ()

