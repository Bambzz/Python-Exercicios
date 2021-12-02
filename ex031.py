dist = float(input('Qual a distância da viagem?'))
if dist <= 200:
    print('sua viagem irá custar {} reais'.format(dist*0.5))
else:
    print('sua viagem irá custar {} reais'.format(dist*0.45))

