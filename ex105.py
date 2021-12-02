def notas(* num, sit=False):
    '''Função recebe varias notas e faz uma análise
    parâmetro "sit" define se deseja ou não a situação da média das notas'''
    alunos = {}
    maior = menor = cont = media = 0
    for nota in num:
        media += nota
        cont += 1
        if cont == 1:
            maior = nota
            menor = nota
        elif maior < nota:
            maior = nota
        elif menor > nota:
            menor = nota
    media /= len(num)
    if media < 5:
        situação = 'Ruim'  
    elif 6 > media > 5:
        situação = 'Razoável'
    elif 8 > media > 6 :
        situação = 'Bom'
    elif media > 8:
        situação = 'Ótimo'
    alunos['total'] = len(num)
    alunos['maior'] = maior
    alunos['menor'] = menor
    alunos['media'] = media
    if sit:
        alunos['situação'] = situação 
    return alunos


n = notas(9, 0, 8, 5.5, 6.8, 4, 10, 9.5, sit=True)
print(n)


