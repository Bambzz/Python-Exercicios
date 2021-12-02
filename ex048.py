soma = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 != 0:
        cont = cont + 1
        soma = soma + c
print('a soma de todos o valores é {}'.format(soma))
print(f'foram {cont}  números')





