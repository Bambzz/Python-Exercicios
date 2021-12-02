Continuar = 's'
Lista = []
while Continuar in 's':
    valor = int(input('Digite um valor'))
    if valor not in Lista:
        print('Valor adicionado com sucesso!!!!')
        Lista.append(valor)
        Continuar = str(input('Deseja continuar?')).lower().strip()[0]
    else:
        print('Valor não adicionado')
Lista.sort()
print(f'Você digitou os valores {Lista}')

