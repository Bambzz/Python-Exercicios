from time import sleep
from random import randint
print('=-' * 13)
print('PALPITES PARA MEGA-SENA')
print('=-' * 13)
num = int(input('Quantos Jogos deseja sortear?'))
Jogo = list()
for c in range(0, num):
    cont = 0
    Jogo.append(list())
    while True:
        pc = randint(1, 60)
        if pc not in Jogo[c]:
            Jogo[c].append(pc)
            cont += 1
        if cont >= 6:
            break
for m in range(0, num):
    sleep(0.8)
    print(f'Gerando números...{sorted(Jogo[m])}')
print(f'-------------- Boa sorte!!! ----------------')
