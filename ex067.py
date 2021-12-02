while True:
    num = int(input('Tabuada, Digite um valor'))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('ACABOU, VOLTE SEMPRE')
