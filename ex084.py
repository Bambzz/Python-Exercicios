Pessoas = []
Adic = []
pesada = leve = cont = 0
while True:
    Adic.append(str(input('Nome   ')))
    Adic.append(float(input('Peso   ')))
    Pessoas.append(Adic[:])
    cont += 1
    if cont == 1:
        leve = Adic[1]
        pesada = Adic[1]
    else:
        if Adic[1] < leve:
            leve = Adic[1]
        elif Adic[1] > pesada:
            pesada = Adic[1]
    Adic.clear()
    continuar = str(input('Continuar? [S/N]')).lower().strip()[0]
    if continuar == 'n':
        break
print(f'no total, são {cont} pessoas cadastradas')
print(f'as pessoas mais pesadas pesaram {pesada}kg e elas são...', end=' ')
for p in Pessoas:
    if p[1] == pesada:
        print(f'{p[0]}', end=' ')
print()
print(f'e as pessoas mais leves pesaram {leve}kg e elsas são...', end=' ')
for l in Pessoas:
    if l[1] == leve:
        print(f'{l[0]}', end=' ')
