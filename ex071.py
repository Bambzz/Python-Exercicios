print('=-' * 24)
print('        Bem Vindo ao Caixa eletrônico')
print('=-' * 24)
cont50 = cont20 = cont10 = cont1 = 0
print()
valor = int(input('Qual o valor a ser sacado?'))
while valor - 50 >= 0:
    valor -= 50
    cont50 += 1
while valor - 20 >= 0:
    valor -= 20
    cont20 += 1
while valor - 10 >= 0:
    valor -= 10
    cont10 += 1
while valor - 1 >= 0:
    valor -= 1
    cont1 += 1
if cont50 > 0:
    print(f'foram utilizadas {cont50} cédulas de 50')
if cont20 > 0:
    print(f'foram utilizadas {cont20} cédulas de 20')
if cont10 > 0:
    print(f'foram utilizadas {cont10} cédulas de 10')
if cont1 > 0:
    print(f'foram utilizadas {cont1} cédulas de 1')
