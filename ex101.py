def Voto(idade):
    if idade < 16:
        return('Não vota')
    elif idade >= 18 and idade < 65:
        return('Voto obrigatório')
    elif idade >= 16 and idade < 18 or idade >= 65:
        return('Voto Opcional')

    
idade = 2021 - (int(input('Qual o ano de seu nascimento? ')))
Vota = Voto(idade)
print(f'Com {idade} anos: {Vota} ')

