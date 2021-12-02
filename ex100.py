from time import sleep
from random import randint
numeros = list()


def sorteia():
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        print(f'{num} ', end='')
        numeros.append(num)
        sleep(0.3)


def somaPar():
    somapar = 0
    for p in range(0, len(numeros)):
        if numeros[p] % 2 == 0:
            somapar += numeros[p]
    print('\n', end='')
    print(f'a soma de todos os números pares sorteados {numeros} é de {somapar}')


sorteia()
somaPar()


