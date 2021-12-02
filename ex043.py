peso = float(input('Qual seu peso?'))
alt = float(input('Qual a sua altura?'))
IMC = peso / (alt * alt)
if IMC <= 18.5:
    print('você está abaixo do peso')
elif 18.5 < IMC <= 25:
    print('você está no peso ideal')
elif 25 < IMC <= 30:
    print('você está acima do peso')
elif 30 < IMC <= 40:
    print('você está obeso')
elif 40 < IMC:
    print('você tem obesidade mórbida')
print('seu IMC {:.2f}'.format(IMC))

