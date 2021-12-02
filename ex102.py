def fatorial(num, show=False):

    '''Calcula o fatorial de um número
       Para "n" o número a ser calculado
       Para "show" a opção de ser mostrado o cálculo ou não'''

    if show == None or show == False:
        from math import factorial
        print(factorial(num))
    elif show:
        n1 = num
        n2 = num - 1
        for c in range(n2, 1, -1):
            print(n1, end=', ')
            n1 *= c
        print(n1)
    print('=-' * 20)
    print('Fim')

fatorial(9)
