valor = float(input('qual o valor do produto?'))
pagamento = int(input('qual a forma de pagamento? (escolha uma alternativa, e digite 1, 2, 3 ou 4)'
                      '\n 1-dinheiro/cheque (\33[32m10%\33[m desc)\n 2-a vista no cartão (\33[32m5%\33[m desc)'
                      '\n 3-cartão em 2x (\33[1;33mpreço normal\33[m)'
                      '\n 4-cartão em 3x ou mais (\33[31mjuros 20%\33[m)'))
if pagamento == 1:
    print('\33[32mO valor com 10% de desconto seria {:.2f} reais\33[m'.format(valor - valor * 10 / 100))
elif pagamento == 2:
    print('\33[32mO valor com 5% de desconto fica {:.2f} reais'.format(valor - valor * 5 / 100))
elif pagamento == 3:
    print('\33[33mO valor fica {:.2f} reais, pois não possui desconto em 2x\33[m'.format(valor))
elif pagamento == 4:
    print('\33[31mO valor em 3x possui 20 % de juros e fica {:.2f} reais\33[m'.format(valor + valor * 20 / 100))
