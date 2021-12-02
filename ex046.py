from time import sleep
resposta = int(input('digite 1 para começar'))
if resposta == 1:
    print('=-' * 14)
    print('\33[31mCONTAGEM PARA O ANO NOVO!!!\33[m')
    print('-=' * 14)
    for c in range(10, 0, -1):
        print(c)
        sleep(1)
    print('\33[36mFELIZ ANO NOVO!!!!')


