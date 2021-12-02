from random import choice
player = str(input('JOKENPO, Você escolhe pedra, papel, ou tesoura?')).lower()
pc = choice(['pedra', 'papel', 'tesoura'])
if pc == 'papel':
    if player == 'tesoura':
        print(f'o computador escolheu {pc}, você ganhou!!')
    if player == 'pedra':
        print(f'o computador escolheu {pc}, você perdeu :(')
    if player == 'papel':
        print(f'o computador também escolheu {pc}, foi um empate')
if pc == 'pedra':
    if player == 'papel':
        print(f'o computador escolheu {pc}, você ganhou!!')
    if player == 'tesoura':
        print(f'o computador escolheu {pc}, você, perdeu :(')
    if player == 'pedra':
        print(f'o computador também escolheu {pc}, foi um empate')
if pc == 'tesoura':
    if player == 'pedra':
        print(f'o computador escolheu {pc}, você ganhou!!')
    if player == 'papel':
        print(f'o computador escolheu {pc}, você perdeu :(')
    if player == 'tesoura':
        print(f'o computador também escolheu {pc}, foi um empate')











