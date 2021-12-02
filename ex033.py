n1 = int(input('digite um número'))
n2 = int(input('digite outro número'))
n3 = int(input('digite mais um número'))
if n1 < n2:
    if n2 > n3:
        print('seu maior número é {}'.format(n2))
    if n1 < n3:
        print('seu menor número é {}'.format(n1))
if n2 < n3:
    if n2 < n1:
        print('seu menor número é {}'.format(n2))
    if n3 > n1:
        print('seu maior número é {}'.format(n3))
if n3 < n1:
    if n3 < n2:
        print('seu menor número é {}'.format(n3))
    if n1 > n2:
        print('seu maior número é {}'.format(n1))






