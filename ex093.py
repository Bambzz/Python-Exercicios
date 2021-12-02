from time import sleep
jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Qual o nome do jogador?'))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols o jogador fez na partida {c + 1}')))
    total += gols[c]
for y in range(0, partidas):
    print(f'na partida {y + 1}, {jogador["nome"]} fez {gols[y]}')
    sleep(1)
jogador['gols'] = gols
print(jogador)
print(f'durante todo o campeonato, {jogador["nome"]} fez {total} gols')
