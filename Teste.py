lista_dados_alunos = [['Natalia', 927602856, '16/06/2006'], ['Pedro', 876237940, '07/12/2005'], ['Claudio', 569713428, '08/02/2003'],
['Mario', 746298370, '28/08/2005']]
alunos = []


def email(nome, matric, nasc):
    aluno = {}
    aluno['nome'] = nome
    aluno['email'] = f'{matric}@estudante.sed.sc.gov.br'
    aluno['senha'] = nasc.replace('/', '')
    alunos.append(aluno
        )


for al in range(0, len(lista_dados_alunos)):
    email(lista_dados_alunos[al][0], lista_dados_alunos[al][1], lista_dados_alunos[al][2]
    )

for c in range(0, len(alunos)):
    print(f'O aluno {alunos[c]["nome"]}, tem o e-mail [{alunos[c]["email"]}] e a senha [{alunos[c]["senha"]}]')

