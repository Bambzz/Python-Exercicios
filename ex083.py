num = str(input('Digite a expressão'))
abre = num.count('(')
fecha = num.count(')')
if abre == fecha:
    print('pode ser uma expressão')
else:
    print('não pode ser uma expressão')