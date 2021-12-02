total = 0
nomemenor = ' '
menor = 0
maisdemil = 0
cont = 0
while True:
    print('=-' * 15)
    print('LOJA DO TIÃO')
    print('=-' * 15)
    produto = str(input('Qual o nome do produto?'))
    preco = float(input('Qual o valor do produto?'))
    total += preco
    cont += 1
    if cont == 1:
        menor = preco
        nomemenor = produto
    if preco < menor:
        menor = preco
        nomemenor = produto
    if preco > 1000:
        maisdemil += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar?')).strip().lower()[0]
    if continuar == 'n':
        break
()
print(f'o Total gasto foi {total}')
print(f'ao todo {maisdemil} produtos custaram mais de mil reais')
print(f'o produto mais barato foi {nomemenor} e custou {menor} reais ')
