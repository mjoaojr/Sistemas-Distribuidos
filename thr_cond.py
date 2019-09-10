import threading

def faza ():
    return conta == 0

def fazb ():
    return contb == 1

def funca ():
    global conta
    global contb
    for i in range (30):
        with cv:
            print ("A")
            conta +=1
            if conta == 3:
                contb = 1
                cv.notify_all ()
                cv.wait_for (faza)

def funcb ():
    global conta
    global contb
    for i in range (10):
        with cv:
            cv.wait_for (fazb)
            contb = 0
            print ("B")
            conta = 0
            cv.notify_all ()


conta = 0
contb = 0
cv = threading.Condition ()

