from socket import *
from threading import *
from random import *

s = socket()

servidor = "0.0.0.0"
porta = 1234
s.bind((servidor, porta))
s.listen(10)

def verifica_vencedor (jog1, jog2):
    if jog1 == jog2:
        return 0
        
    if jog1 == "PEDRA":
        if jog2 == "TESOURA":
            return 1
        else:
            return 2

    if jog1 == "PAPEL":
        if jog2 == "PEDRA":
            return 1
        else:
            return 2

    if jog1 == "TESOURA":
        if jog2 == "PAPEL":
            return 1
        else:
            return 2

def trata_conn (conn, cliente):
    global mutex
    global jogadores
    
    jogadas = {0: "PEDRA", 1: "PAPEL", 2:"TESOURA"}

    data = conn.recv(4096)
    jogador = data.decode()
    print (f"{jogador} se conectou de {cliente}")
    conn.send (str.encode(f"Bem vindo {jogador}"))

    with mutex:
        if not jogador in jogadores:
            jogadores[jogador] = 0
    
    vencidas = jogadores[jogador]

    placar = [0,0]
    while True:
        data = conn.recv(4096)
        if data == b'':
            break
        jogada = data.decode()
        print(f"Jogador {jogador} mandou {jogada}")
        minhajog = jogadas[randint(0,2)]
        print(f"joguei {minhajog}")
        conn.send (str.encode(minhajog))
        vencedor = verifica_vencedor (jogada, minhajog)
        print(f"vencedor: {vencedor}")

        
        if vencedor == 0:
            continue
        placar[vencedor-1] += 1
        
        if 3 in placar:
            break
        
    if placar[0] == 3:
        vencidas += 1

    with mutex:
        jogadores[jogador] = vencidas

    print(f"{jogador} venceu {vencidas}")
    data = conn.recv(4096)
    conn.send (str.encode(f"{vencidas}"))

    print (f"Fim da conexão")
    conn.close ()

print (f"Servidor no ar...")
mutex = Lock()
cont_t = 0
jogadores = {}

while True:
    (conn, cliente) = s.accept ()
    
    t = Thread(target=trata_conn, args=(conn,cliente))
    t.start()
    cont_t += 1
    print(f"Já disparei {cont_t} threads até agora.")