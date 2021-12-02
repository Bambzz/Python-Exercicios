pessoa = dict()
while True:
    pessoa['nome'] = str(input('Qual o seu nome?'))
    pessoa['anonasc'] = int(input('Qual o ano de seu nascimento?'))
    pessoa['cart'] = int(input('Carteira de trabalho (0 não tem)'))
    if pessoa['cart'] == 0:
        break
    pessoa['anocont'] = int(input('Qual o ano de sua contratação?'))
    pessoa['salario'] = float(input('Qual o seu salário?'))
    break
for c in range(0, 1):
    print(f'o nome tem o valor {pessoa["nome"]}'
          )
    print(f'idade tem o valor {2021 - pessoa["anonasc"]}'
          )
    print(f'ctps tem o valor {pessoa["cart"]}'
          )
    if pessoa['cart'] == 0:
        break
    print(f'contratação tem o valor {pessoa["anocont"]}, e já contribuiu em {2021 - pessoa["anocont"]} anos'
          )
    print(f'salario tem o valor {pessoa["salario"]}'
          )
    if 2021 - pessoa['anocont'] > 35:
        print(f'você já pode se aposentar!!'
              )
    elif 2021 - pessoa['anocont'] < 35:
        print(f'você só vai poder se aposentar quando tiver '
              f'{(35 - (2021 - pessoa["anocont"])) + (2021 - pessoa["anonasc"])} anos')


