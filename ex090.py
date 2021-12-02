Dic = dict()
Dic['Nome'] = str(input('Qual o nome do aluno?'))
Dic['Media'] = float(input(f'Qual a média de {Dic["Nome"]}?'))
print(f'o nome é igual a {Dic["Nome"]}')
print(f'a média é igual a {Dic["Media"]}')
if Dic['Media'] < 7:
    print('a situação é igual a Reprovado')
else:
    print('a situação é igual a Aprovado')
