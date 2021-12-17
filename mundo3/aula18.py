from random import randint
from time import sleep
# exercicio 84
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('=' * 20)
print(f'Os daados foram {princ}')
print(f'Ao todo foram cadastrados {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')

# exercicio 85
num = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')

# exercicio 86
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(
            input(f'Digite um valor para a posicao [{l},{c}]: '))
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()

# exercicio 87
par = mai = scol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(
            input(f'Digite um valor para a posicao [{l},{c}]: '))
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos valores pares e {par}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma do valores da terceira coluna e {scol}')
for c in range(0, 3):
    if matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha e {mai}')

# exercicio 88
print('--' * 10)
print(f'JOGA NA MEGA SENA')
print('--' * 10)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
lista = list()
jogos = list()
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

# exercicio 89
ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual alluno? (-1 interronpe): '))
    if opc == -1:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
