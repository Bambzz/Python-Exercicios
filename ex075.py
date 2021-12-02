num = (int(input('Digite um número')),
       int(input('Digite um número')),
       int(input('Digite um número')),
       int(input('Digite um número')))
print(f'você digitou os valores {num}')
print(f'o número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o número 3 apareceu na posição {num.index(3) + 1}')
else:
    print('o número 3 não apareceu!!')
print(f'os números pares são ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=', ')
