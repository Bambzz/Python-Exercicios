n1 = float(input('primeiro lado do triangulo'))
n2 = float(input('segundo lado do triangulo'))
n3 = float(input('terceiro lado do triangulo'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('você pode formar um triângulo')
else:
    print('você não pode format um triângulo')
    exit()
if n1 == n2 == n3:
    print('esse é um triângulo equilátero')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('esse é um triângulo isósceles')
elif n1 != n2 != n3:
    print('esse é um triângulo escaleno')
else:
    print('você não pode format um triângulo')
