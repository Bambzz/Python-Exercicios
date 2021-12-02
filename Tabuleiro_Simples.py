from random import randint, choice
from os import system

# Para dois jogadores, pois a parce do "PC" ainda não foi automatizada

Jogadores= ['PC', 'PLAYER']
JogadorAtual = choice(Jogadores)
VoltasPc = 0
VoltasPlayer = 0
PosicaoPc = 0
PosicaoPlayer = 0
PlayerMoney = 20
PcMoney = 20
PosicoesTotais = 16
NumDado = 0
cont = 0


# Eventos


def Anda():
    global VoltasPc
    global VoltasPlayer
    global PosicoesTotais
    global PosicaoPlayer
    global PosicaoPc
    global JogadorAtual
    global NumDado
    NumDado = randint(1, 7)
    if JogadorAtual == 'PC':
        PosicaoPc += NumDado
        if PosicaoPc >= PosicoesTotais:
            PosicaoPc -= PosicoesTotais
            VoltasPc += 1
    elif JogadorAtual == 'PLAYER':
        PosicaoPlayer += NumDado
        if PosicaoPlayer >= PosicoesTotais:
            PosicaoPlayer -= PosicoesTotais
            VoltasPlayer += 1


def TrocaDeVez():
    global JogadorAtual
    if JogadorAtual == 'PC':
        JogadorAtual = 'PLAYER'
    elif JogadorAtual == 'PLAYER':
        JogadorAtual = 'PC'


def Jogada(y):
    global JogadorAtual
    global NumDado
    if y == 1:
        Anda()
    elif y == 2:
        Sorte()


def Sorte():
    global PcMoney
    global PlayerMoney
    global JogadorAtual
    if JogadorAtual == 'PC':
        sorte = randint(0, 11)
        if sorte >= 4:
            PcMoney *= 2
        elif sorte < 4:
            PcMoney /= 2
    elif JogadorAtual == 'PLAYER':
        sorte = randint(0, 11)
        if sorte >= 4:
            PlayerMoney *= 2
        elif sorte < 4:
            PlayerMoney /= 2


# Programa principal, com "interface gráfica"
while True:

    if cont == 0:
        system('clear')
    if cont >= 1:
        print('=-' * 20)
        if JogadorAtual == 'PC':
            print(f'Jogador Atual = \33[1;31m{JogadorAtual}\33[m')
        elif JogadorAtual == 'PLAYER':
            print(f'Jogador Atual = \33[1;32m{JogadorAtual}\33[m')
        print(f'Jogada número {cont}')
    if cont >= 1:
        Jogada(int(input('Qual a sua jogada? (1 para o dado, 2 para tentar a sorte) ')))
    if cont >= 1:
        system('clear')
    print(f'Dado = {NumDado}')
    print(f'\33[0;32mPlayerMoney\33[m = {PlayerMoney}')
    print(f'\33[0;31mPcMoney\33[m = {PcMoney}')
    print(f'\33[0;32mPlayer está na posição\33[m {PosicaoPlayer}\33[0;32m e na volta\33[m {VoltasPlayer}')
    print(f'\33[0;31mPC está na posição\33[m {PosicaoPc}\33[0;31m e na volta\33[m {VoltasPc}')
    if PlayerMoney > 1000:
        print('O PLAYER GANHOU, POIS FICOU RICO')
        break
    elif PlayerMoney < 1:
        print('O PLAYER PERDEU, POIS FICOU POBRE')
        break
    if PcMoney > 1000:
        print('O PC GANHOU, POIS FICOU RICO')
        break
    elif PcMoney < 1:
        print('O PC PERDEU, POIS FICOU POBRE')
        break
    if VoltasPc > 5:
        print('O PC GANHOU, POIS COMPLETOU 6 VOLTAS')
        break
    if VoltasPlayer > 5:
        print('O PLAYER GANHOU, POIS COMPLETOU 6 VOLTAS')
        break
    cont += 1    
    TrocaDeVez()
