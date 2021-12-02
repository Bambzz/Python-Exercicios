from random import choice
npc = str(choice([0, 1, 2, 3, 4, 5]))
ppc = str(input('digite um número de 0 a 5'))
if ppc == npc:
    print('você acertou, o número escolhido era {} Parabéns'.format(npc))
else:
    print('você errou, o número era {}'.format(npc))