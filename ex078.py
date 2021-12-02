lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para ser colocado na posição {c}')))
print(lista)
print(f'o maior valor foi de {max(lista)} na posição {lista.index(max(lista))}')
print(f'o menor valor foi de {min(lista)} na posição {lista.index(min(lista))}')
