print('SEQUÊNCIA DE FIBONACCI')
print('=-' * 17)
n = int(input('Quantos termos deseja mostrar?'))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 2
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1




