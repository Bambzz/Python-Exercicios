from time import sleep


def maior(* num):
    cont = maiorvalor = 0
    sleep(0.5)
    for valor in num:
        cont += 1
        if valor > maiorvalor:
            maiorvalor = valor
    print(f'Analisando os valores, vemos que temos {cont} valores, e o maior é {maiorvalor}')
    for valor in num:
        sleep(0.3)
        print(valor, end=' ',)
    print('\n', end='')
    print('+=-' * 15)


maior(0, 5, 6, 8)
maior(6, 7, 4, 9, 3, 1, 2)
maior(4, 5)
maior()
