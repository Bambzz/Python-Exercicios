sal = float(input('digite seu salário'))
sal10 = (sal*10 / 100) + sal
sal15 = (sal*15 / 100) + sal
if sal >= 1250.00:
    print(f'\33[7;35;41m seu salário com aumento é {sal10}\33[m')
else:
    print(f'seu salário com aumento é {sal15}')






