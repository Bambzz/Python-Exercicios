mulher20 = 0
homem = 0
pessoa18 = 0
while True:
    sexo = int(input('Você é homem ou mulher? [1] para homem e [2] para mulher'))
    idade = int(input('Quantos você tem?'))
    if sexo == 1:
        homem += 1
    if sexo == 2 and idade < 20:
        mulher20 += 1
    if idade >= 18:
        pessoa18 += 1
    continuar = int(input('deseja continuar? [1] para sim, [2] para não'))
    if continuar == 2:
        break
print(f'AO TOTAL\n {pessoa18} pessoas tem mais de 18 anos\n {mulher20}'
      f' mulheres tem menos de 20 anos\n {homem} das pessoas são homens ')