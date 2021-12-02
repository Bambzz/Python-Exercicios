def LeiaInt(pergunta):
    while True:
        n = input(f'{pergunta}')
        enum = n.isnumeric()
        if enum:
            n = int(n)
            return n 
        else:
            print('Erro, Digite um número')
            
num = LeiaInt('Digite um número ')
print(f'você digitou o número {num}')