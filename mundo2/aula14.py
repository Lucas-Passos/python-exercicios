from random import randint
from time import sleep
# exercicio 57
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por Favor, informe seu sexo: ')
               ).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

# exercicio 58
print('Estou pensando em um numero entre 0 e 10 tente adivinhar')
num = randint(0, 10)
palpites = 0
acertou = False
while not acertou:
    player = int(input('Qual seu palppite? '))
    palpites += 1
    if player == num:
        acertou = True
    else:
        if player < num:
            print('Mais... Tente novamente.')
        elif player > num:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas!'.format(palpites))

# exercicio 59
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = False
res = 0
while not sair:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos valores')
    print('[ 5 ] sair do programa')
    ops = int(input('Qual e a sua opcao? '))
    if ops == 1:
        res = n1 + n2
        print('A soma entre {} + {} e {}'.format(n1, n2, res))
    elif ops == 2:
        res = n1 * n2
        print('O resultado de {} x {} e {}'.format(n1, n2, res))
    elif ops == 3:
        if n1 > n2:
            res = n1
            print('O maior valor e {}'.format(res))
        elif n1 == n2:
            print('Os valores sao iguais')
        else:
            res = n2
            print('O maior valor e {}'.format(res))
    elif ops == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif ops == 5:
        sair = True
        print('Finalizando')
    else:
        print('Opcao Ivalida. Tente novamente')
    print('=-=' * 10)
sleep(1)
print('Programa Finalizado!')

# exercicio 60
num = int(input('Digite um numero para calcular seu Fatorial: '))
c = num
fac = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    fac *= c
    c -= 1
print(' {}'.format(fac))

# exercicio 61
print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

# exercicio 62
print('Gerador de PA 2')
print('=' * 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end="")
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja ver mais termos? '))
print('Progressao finalizada com {} termos mostrados'.format(total), end='')

# exercicio 63
print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} > {}'.format(t1, t2), end='')
while cont <= n:
    cont += 1
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' > FIM')

# exercicio 64
n1 = total = cont = 0
n1 = int(input('Digite um numero [999 para parar]: '))
while n1 != 999:
    cont += 1
    total += n1
    n1 = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, total))

# exercicio 65
resp = 'Ss'
quant = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
