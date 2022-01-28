import urllib
import urllib.request
'''#exercicio 113
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digte um numero inteiro valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuario decidiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero real valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mO usuario dicidiu nao digitar esse numero. \033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi: {n1} e o valor real foi {n2}')'''

'''exercicio 114
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta acessivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')'''