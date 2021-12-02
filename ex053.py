frase = str(input('Digite uma frase'))
SemEspacos = frase.replace(' ', '').lower()
invert = SemEspacos[::-1]
if SemEspacos == invert:
    print('a frase {}, é um palíndromo'.format(frase))
else:
    print('a frase {}, não é um palíndromo'.format(frase)
          )
print(SemEspacos
      )
print(invert
      )

