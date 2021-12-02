pessoas = dict()
povo = list()
cont = totidade = media = 0
mulheres = []
acimaDaMedia = []
while True:
    pessoas['nome'] = str(input('Qual o nome da pessoa?'))
    while True:
        pessoas['sexo'] = str(input('Qual o sexo da pessoa?')).lower().strip()[0]
        if pessoas['sexo'] not in 'mf':
            print('Erro, tente novamente')
        if pessoas['sexo'] in 'f':
            mulheres.append(pessoas['nome'])
            break
        elif pessoas['sexo'] in 'mf':
            break
    while True:
        idade = (input('Qual a idade da pessoa?'))
        if idade.isnumeric():
            pessoas['idade'] = int(idade)
            break
        else:
            print('Erro, por favor responda com um número')
    cont += 1
    totidade += pessoas['idade']
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
        if continuar not in 'sn':
            print('Erro, Por favor responda só Sim ou Não')
        else:
            break
    media = totidade / cont
    povo.append(pessoas.copy())
    pessoas.clear()
    if continuar == 'n':
        break
print(povo)
for c in range(0, cont):
    if povo[c]['idade'] > media:
        acimaDaMedia.append((povo[c]['nome']))
print(f'ao total foram cadastradas {cont} pessoas')
print(f'a média de idade do grupo foi {media}')
print(f'as mulheres foram {mulheres}')
print(f'as pessoas com idade acima da média foram {acimaDaMedia}')

