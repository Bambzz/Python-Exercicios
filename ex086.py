linha = coluna = cont = 0
m = [[], [], [], [], [], [], [], [], []]
for c in range(0, 9):
    valor = int(input(f'Digite o valor para ser colocado na posição [{linha}, {coluna}]'))
    if coluna < 2:
        coluna += 1
    else:
        coluna = 0
        linha += 1
    m[c].append(valor)
print('   0    1    2')
print(f'0 {m[0]}  {m[1]}  {m[2]}\n1 {m[3]}  {m[4]}  {m[5]}\n2 {m[6]}  {m[7]}  {m[8]}')

