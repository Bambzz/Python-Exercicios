sexo = str(input('Digite seu sexo')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo')).upper()
if sexo == 'M' or sexo == 'F':
    print('Seu sexo é {}'.format(sexo))
