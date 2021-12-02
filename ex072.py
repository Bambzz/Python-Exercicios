num = int(input('digite um número de 0 a 20'))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número de 0 a 20'))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'o número digitado foi {extenso[num]}')
