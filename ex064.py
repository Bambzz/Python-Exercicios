num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número'))
    soma += num
    cont += 1
print('a soma entre eles foi {}'.format(soma - 999))
print('e foram {} números'.format(cont))
