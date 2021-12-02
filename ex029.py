vel = int(input('qual a velocidade do carro'))
multa = (vel-80)*7
if vel <= 80:
    print('parabéns, você está abaixo do limite, não será multado')
else:
    print('você está acima do limite, sua multa será de {} reais'.format(multa))

