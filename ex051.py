PrimeiroTermo = int(input('Digite o primeiro termo da PA'))
razao = int(input('Digite a razão'))
decimo = PrimeiroTermo + (10 - 1) * razao
for c in range(PrimeiroTermo, decimo, razao):
    print(c)
