def frase(b):
    print('~' * (len(b) + 4))
    print(f'  {b}')
    print('~' * (len(b) + 4))


while True:
    frase(str(input('Digite sua frase para que ela apareça com linhas')))
    continuar = str(input('Continuar?')).lower().strip()[0]
    if continuar == 'n':
        break
