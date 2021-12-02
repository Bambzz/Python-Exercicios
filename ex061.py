primeiro = int(input('digite o primeiro termo da PA'))
razao = int(input('digite a razão'))
c = 1
termo = primeiro
while c <= 10:
    termo += razao
    print(termo)
    c += 1
