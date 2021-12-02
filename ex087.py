# Alimenta a Matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para {linha}, {coluna}\n'))

# Mostra a Matriz
print('=-' * 14)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

# Analisa
totalpar = totcoluna3 = maiorlinha2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            totalpar += matriz[linha][coluna]
        if coluna == 2:
            totcoluna3 += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maiorlinha2:
                maiorlinha2 = matriz[linha][coluna]

# Resultados
print(f'a soma de números pares na matriz foi de {totalpar}')
print(f'a soma dos valores da terceira coluna foi de {totcoluna3}')
print(f'o maior valor da segunda linha foi de  {maiorlinha2}')


