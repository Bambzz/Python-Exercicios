num = int(input('Digite um número'))
mult = 0
if num == 2:
    print('é primo')
elif num % 2 != 0:
    for c in range(1, num + 1):
        div = num % c
        if div == 0:
            mult = mult + 1
    if mult == 2:
        print('é primo')
    else:
        print('não é primo')
else:
    print('números pares não podem ser primos, exceto o número 2')
