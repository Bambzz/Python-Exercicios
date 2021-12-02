continuar = 's'
Lista = []
Par = []
Impar = []
while continuar == 's':
    num = int(input('Digite um número'))
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
    Lista.append(num)
    if num % 2 == 0:
        Par.append(num)
    elif num % 2 != 0:
        Impar.append(num)
print(f'os números digitados foram {Lista}')
print(f'os números ímpares digitados foram {Impar}')
print(f'os números pares digitados foram {Par}')
