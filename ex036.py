ValorDaCasa = float(input('Qual o Valor da Casa? '))
Salario = float(input('Qual seu salário? '))
Tempo = float(input('Em quantos Anos deseja pagar? '))*12
PorcentagemSalario = Salario * 30 / 100
Parcelas = ValorDaCasa / Tempo
if PorcentagemSalario > Parcelas:
    print('Você irá pagar sua casa no valor de {:.0f} reais em {:.0f} Parcelas '
          'de {:.2f} reais por mês'.format(ValorDaCasa, Tempo, Parcelas))
else:
    print('Desculpe, Você Não pode financiar a casa')
