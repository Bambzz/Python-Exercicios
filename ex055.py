maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input(f'peso da {p+1} pessoa'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'a pessoa mais pesada pesa {maior}, e a mais leve pesa {menor}')

