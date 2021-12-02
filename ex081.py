continuar = 's'
Lista = []
while continuar == 's':
    Lista.append(int(input('Digite um número')))
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
Lista.sort(reverse=True)
print(f'Você digitou {len(Lista)} elementos')
print(f'Em ordem decresente, os valores são {Lista}')
if 5 in Lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
