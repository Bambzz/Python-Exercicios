n1 = float(input('qual sua primeira nota'))
n2 = float(input('qual sua segunda nota'))
media = (n1 + n2) / 2
if media < 5.0:
    print('VOCÊ FOI REPROVADO COM MEDIA {:.2f}, BURRÃO DMS'.format(media))
elif 5.0 < media < 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO, COM MÉDIA {:.2f}, BOA SORTE'.format(media))
else:
    print('VOCÊ FOI APROVADO COM MÉDIA {:.2f}, PARABÉNS'.format(media))
