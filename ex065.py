num = int(input('Digite um número'))
continuar = int(input('Deseja continuar? digite qualquer número para sim, [0] para não'))
maior = num
menor = num
soma = num
qntnum = 1
media = 0
while continuar != 0:
    num = int(input('Digite um número'))
    continuar = int(input('Deseja continuar? digite qualquer número para sim, [0] para não'))
    qntnum += 1
    soma += num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
media = soma / qntnum
print('ao total foram {} números, e a média deles foi {}, o maior foi {} '
      'e o menor foi {}'.format(qntnum, media, maior, menor))
