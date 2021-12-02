jogador = dict()
jogadores = list()
gols = list()
cont = 0
while True:
    print('=-' * 14)
    jogador['nome'] = str(input('Qual o nome do jogador?'))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c+1}')))
    jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    continuar = 'a'
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar?')).lower().strip()[0]
    if continuar == 'n':
        print('x-=_=-' * 10)
        break
print('cod  nome            gols          total')
for j in range(0, len(jogadores)):
    print(f' {j}   {jogadores[j]["nome"]:<16}{jogadores[j]["gols"]}          {sum(jogadores[j]["gols"])}')
# FODASE TA BÃO ASSIM KK
