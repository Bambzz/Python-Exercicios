Alunos = list()
cont = 0
while True:
    aluno = str(input('Nome do Aluno'))
    nota1 = float(input('Nota 1'))
    nota2 = float(input('Nota 2'))
    Alunos.append(list())
    Alunos[cont].append(aluno)
    Alunos[cont].append(list())
    Alunos[cont][1].append(nota1)
    Alunos[cont][1].append(nota2)
    cont += 1
    continuar = str(input('Deseja continuar?')).strip().lower()[0]
    if continuar == 'n':
        break
print(Alunos)
for c in range(0, len(Alunos)):
    print(f'média aluno {c} --> {Alunos[c][0]} : {(Alunos[c][1][0] + Alunos[c][1][1]) / 2}')
while True:
    mostrar = int(input('Deseja mostrar as notas de qual aluno?(999 interrompe)'))
    print(f'as notas de {Alunos[mostrar][0]} são {Alunos[mostrar][1]}')
    if mostrar == 999:
        break

