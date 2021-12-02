nome = str(input('Qual seu nome completo?'))
Str = nome.strip()
Spl = Str.split()
primeironome = len(Spl[0])
segundonome = len(Spl[1])
tudo = primeironome+segundonome
# ----------------------------------------------------------------------------------------------------------------------
print('seu nome em maiúsculo é {}'.format(Str.upper()))
print('seu nome em minúsculo é {}'.format(Str.lower()))
print('seu primeiro nome tem {} letras'.format(primeironome))
print('seu segundo nome tem {} letras'.format(segundonome))
print('o total de letras de seu nome é {}'.format(tudo))














