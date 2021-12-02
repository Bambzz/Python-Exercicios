from random import choice
pc = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(pc)
player = int(input('digite um número'))
tentativas = 1
while player != pc:
    player = int(input('errou tente outro'))
    tentativas += 1
if player == pc:
    print('acertou, e você precisou de {} tentativas'.format(tentativas))
