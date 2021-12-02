primeiro = (int(input('qual o primeiro termo?')))
razao = int(input('qual a razão?'))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        termo += razao
        cont += 1
        print(f'{termo}---> ', end='')
    mais = (int(input('\nquantos termos você quer a mais?')))
print('FIM')
print('o total de termos foi {}'.format(total))


