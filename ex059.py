while True:
    n1 = int(input('digite um número'))
    n2 = int(input('digite outro número'))
    resposta = int(input(' Digite [1] para somar\n Digite [2] para multiplicar\n Digite [3] para ver qual o maior\n '
                         'Digite [4] para reiniciar\n Digite [5] para sair do programa'))
    if resposta == 1:
        print('a soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif resposta == 2:
        print('a multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif resposta == 3:
        if n1 > n2:
            print('o maior número é {}'.format(n1))
        elif n2 > n1:
            print('o maior número é {}'.format(n2))
        elif n1 == n2:
            print('são iguais')
    elif resposta == 4:
        continue
    elif resposta == 5:
        exit()
