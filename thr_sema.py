from threading import *
import time

sema = Semaphore(3)

def print_hello (tid):
    global sema
    with sema:
        for i in range (5):
            print(f"Sou a thread {tid}.")
            time.sleep(1)
    print (f"Thread {tid} morreu.")
    time.sleep(1)

threads = []
for tid in range (5):
    threads.append(Thread(target=print_hello, args=(tid,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print (f"Thread mãe morreu")
