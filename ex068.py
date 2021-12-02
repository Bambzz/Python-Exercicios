from random import choice
vitorias = 0
soma = 0
while True:
    player = str(input('Par ou ímpar, [P/I]')).lower()
    num = int(input('digite seu número'))
    pc = choice(list(range(1, 10)))
    soma = (num + pc)
    parouimpar = soma % 2
    if player == 'p':
        if parouimpar == 0:
            print(f'Você ganhou!!!, o computador escolheu {pc} e você escolheu {num} a soma foi {soma}, você é PAR')
            vitorias += 1
        else:
            break
    elif player == 'i':
        if parouimpar != 0:
            print(f'Você ganhou!!!, o computador escolheu {pc} e você escolheu {num} a soma foi {soma}, você é ÍMPAR')
            vitorias += 1
        else:
            break
    else:
        print('TENDI NÃO OSH')
print(f'Você perdeu, o computador escolheu {pc} você escolheu {num} '
      f'a soma deu {soma} mas ganhou {vitorias} vezes')
