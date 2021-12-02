def Jogador(jogador=('desconhecido'), gol='0'):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


jogador = str(input('Qual o nome do jogador? '))
gols = str(input(f'Quantos gols {jogador} fez?'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    Jogador(gol=gols)
else:
    Jogador(jogador, gols)
