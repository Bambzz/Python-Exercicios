Nasc = int(input('Qual ano você nasceu?'))
idade = 2021 - Nasc
if idade > 18:
    print('Já passou da hora de se alistar, você está atrasado em {} anos'.format(idade-18))
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar, aguarde'.format(18-idade))
else:
    print('Você deve se alistar esse ano, pois já possui ou vai completar 18 anos')
