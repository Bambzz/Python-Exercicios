cont = 0
soma = 0
while True:
    num = int(input('Digite um valor (digite 999 para parar)'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'no total foram {cont} números e a soma entre eles foi {soma}')
