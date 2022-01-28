from time import sleep
from random import randint
# exercicio 96
def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} e de {a}m².')


print(' Controle de Terrenos')
print('=' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)

#exercicio 97
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Lucas Passos.')
escreva('Curso em Video.')

#exercicio 98
def cont(i, f, p):
    if p <= 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 10)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


cont(1, 10, 1)
cont(10, 0, 2)
print('=' * 10)
print('Agora e sua vez de contar!')
i = int(input('inicio da contagem: '))
f = int(input('fim da contagem: '))
p = int(input('passo da contagem: '))
cont(i, f, p)

# exercicio 99
def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maoir = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
 
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# exercicio 100
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores parea dde {lista}, temos {soma}')



nums = []
sorteia(nums)
somaPar(nums)
