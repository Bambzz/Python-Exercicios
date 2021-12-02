from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
Tupla = n
print(f'os valores sorteados foram {Tupla}')
print(f'o maior valor foi {max(Tupla)}')
print(f'o menor valor foi {min(Tupla)}')
