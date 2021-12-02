Tudo = [[], []]
Par = []
Impar = []
for c in range(1, 8):
    num = int(input('Digite um número'))
    if num % 2 == 0:
        Tudo[0].append(num)
    elif num % 2 != 0:
        Tudo[1].append(num)
Tudo[0].sort()
Tudo[1].sort()
print(f'Os valores pares digitados foram {Tudo[0]}')
print(f'Os valores ímpares digitados foram {Tudo[1]}')
