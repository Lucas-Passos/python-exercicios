from random import randint
# exercicio 66
cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Voce digitou {cont} e a soma deles foi {soma}')

# exericio 67
while True:
    print('=' * 20)
    n = int(input('Digite um valor para ver sua tabuada: '))
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('=' * 20)
print('PROGRAMA ENCERRADO!')

# exercicio 68
v = 0
while True:
    play = int(input('Digite um valor: '))
    comp = randint(0, 11)
    total = play + comp
    op = ' '
    while op not in 'PI':
        op = str(input('Impar ou Par? [I/P] ')).upper().strip()[0]
    print(f'Voce jogou {play} e o computador {comp}. Total de {total}')
    print('PAR' if total % 2 == 0 else 'DEU PAR')
    if op == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif op == 'I':
        if total % 2 != 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')

# exercicio 69
h = m = p = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [F/M] ')).upper().strip()[0]
    if i < 20 and s == 'F':
        m += 1
    if s == "M":
        h += 1
    if i >= 18:
        p += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{m} mulheres tem menos de 20 anos.')
print(f'{p} pessoas tem mais de 18 anos.')
print(f'{h} homens foram cadastrados.')

# exercicio 70
print('-' * 20)
print('LULJA!')
print('-' * 20)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco do produto: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'total gasto R${total:.2f}.')
print(f'{totmil} custam mais de R$1000.')
print(f'{barato} e o produto mais barato custando R${menor:.2f}')

# exercicio 71
print('=' * 20)
print('{:^20}'.format('CAIXA'))
print('=' * 20)
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cedulas de R${ced} ")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 20)
print('FIM DO PROGRAMA!')
