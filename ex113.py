# Começando com try catch


def LeiaInt(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, Digite novamente')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não continuar')
            return n
        else:
            return n
            
    

def LeiaFloat(msg):
    n = 0
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro, Digite novamente')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não continuar')
            return n
        else:
            return n          
        
    
inteiro = LeiaInt('Digite um número Inteiro ')
real = LeiaFloat('Digite Um número Real ')
print(f'Voce digitou os números {inteiro} e {real}')