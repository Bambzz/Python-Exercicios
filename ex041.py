Nasc = int(input('Qual o ano de seu nascimento? '))
idade = 2021 - Nasc
if idade <= 9:
    print('você está na categoria mirim')
elif 9 < idade < 14:
    print('você está na categoria infantil')
elif 14 < idade < 19:
    print('você está na categoria júnior')
elif 19 == idade or idade == 20:
    print('você está na categoria sênior')
else:
    print('você está na categoria master')
