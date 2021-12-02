maior = 0
menor = 0
completa = 0
nemnasceu = 0
for c in range(0, 7):
    anonasc = int(input('qual o ano de seu nascimento?'))
    idade = 2021 - anonasc
    if idade > 18:
        maior = maior + 1
        print(f'a {c+1} pessoa é maior de idade')
    elif anonasc > 2021:
        print(f'ta doido mininu, a {c+1} pessoa ainda nem nasceu')
        nemnasceu = nemnasceu + 1
    elif idade == 18:
        print(f'a {c+1} pessoa completa 18 anos esse ano!!')
        completa = completa + 1
    elif idade < 18:
        menor = menor + 1
        print(f'a {c+1} pessoa é menor de idade')
print(f'Ao total, {maior} pessoas possuiem mais de 18 anos, e {menor} pessoas possuiem menos de 18 anos ')
print(f'e também {completa} pessoas completam 18 anos este ano (ou já completaram)')
if nemnasceu > 0:
    print(f' e {nemnasceu} pessoas ainda 'f'nem nasceram seis tão tudo loco ')
