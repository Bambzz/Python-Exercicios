from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo * -1 > 0:
        passo = passo * -1
    if inicio > fim:
        passo = passo * -1
    print('=-' * 20)
    print(f'     CONTAGEM DE {inicio} A {fim} DE {passo} EM {passo}')
    print('=-' * 20)
    for p in range(inicio, fim, passo):
        sleep(0.3)
        print(p, end=' ')
    print(fim)
    print('=-' * 20)
    sleep(0.5)
    print('                PRÓXIMO')
    sleep(0.5)


contador(1, 10, 1

         )
contador(10, 0, -2

         )
print('AGORA PERSONALIZE A CONTAGEM')
contador(inicio=(int(input('Inicio'))), fim=(int(input('Fim'))), passo=(int(input('Passo'))))

